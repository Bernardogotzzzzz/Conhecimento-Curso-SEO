"""Grava o áudio que sai do alto-falante, uma aula por vez.

Uso:  python gravar.py M04            (grava o módulo inteiro, aula a aula)
      python gravar.py M04 --de A05   (retoma a partir da A05)
      python gravar.py M04 --vel 1.5  (velocidade do player; padrão 2.0)

Por aula: deixe o vídeo pausado, aperte ENTER aqui e IMEDIATAMENTE dê play.
A gravação para sozinha pela duração da aula; ENTER antes disso encerra (aulas sem duração conhecida).
"""
import argparse, json, os, subprocess, sys, threading, time, wave
import pyaudiowpatch as pa

RAIZ = r"D:\ESCOLA DE SEO - Conhecimento extraido"
AUDIOS = os.path.join(RAIZ, "05-AUDIOS")
MARGEM = 6  # segundos extras no fim


def segundos(txt):
    m, s = txt.split(":")
    return int(m) * 60 + int(s)


def gravar(destino_wav, limite):
    p = pa.PyAudio()
    dev = p.get_default_wasapi_loopback()
    canais, taxa = dev["maxInputChannels"], int(dev["defaultSampleRate"])
    wf = wave.open(destino_wav, "wb")
    wf.setnchannels(canais); wf.setsampwidth(2); wf.setframerate(taxa)

    def cb(dados, frames, tempo, status):
        wf.writeframes(dados)
        return (None, pa.paContinue)

    stream = p.open(format=pa.paInt16, channels=canais, rate=taxa, input=True,
                    input_device_index=dev["index"], frames_per_buffer=1024, stream_callback=cb)
    parar = threading.Event()
    threading.Thread(target=lambda: (input(), parar.set()), daemon=True).start()
    t0 = time.time()
    while not parar.is_set() and (limite is None or time.time() - t0 < limite):
        dec = int(time.time() - t0)
        print(f"\r  gravando {dec//60:02d}:{dec%60:02d}" + (f" / {int(limite)//60:02d}:{int(limite)%60:02d}" if limite else "  (ENTER para parar)"), end="", flush=True)
        time.sleep(0.5)
    stream.stop_stream(); stream.close(); wf.close(); p.terminate()
    print()


def comprimir(wav):
    saida = wav.replace(".wav", ".16k.wav")
    subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-ac", "1", "-ar", "16000", saida],
                     creationflags=0).wait()
    os.remove(wav)
    os.replace(saida, wav.replace(".wav", ".final.wav"))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("modulo"); ap.add_argument("--de"); ap.add_argument("--vel", type=float, default=2.0)
    a = ap.parse_args()
    cfg = json.load(open(os.path.join(os.path.dirname(__file__), "aulas.json"), encoding="utf-8"))[a.modulo]
    os.makedirs(AUDIOS, exist_ok=True)
    ligado = a.de is None
    for cod, titulo, dur in cfg["aulas"]:
        if cod == a.de: ligado = True
        if not ligado: continue
        nome = f"{a.modulo}-{cod}"
        if os.path.exists(os.path.join(AUDIOS, nome + ".final.wav")):
            print(f"{nome} já gravada, pulando."); continue
        print(f"\n=== {nome} — {titulo} ({dur or 'duração desconhecida'}) ===")
        input(f"Abra a aula, pause, ajuste {a.vel}x. ENTER aqui e logo em seguida PLAY... ")
        limite = segundos(dur) / a.vel + MARGEM if dur else None
        wav = os.path.join(AUDIOS, nome + ".wav")
        gravar(wav, limite)
        comprimir(wav)
        print(f"  salvo: {nome}.final.wav")
    print("\nMódulo concluído.")
