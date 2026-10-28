"""Transcreve os áudios de 05-AUDIOS para 06-TRANSCRICOES (português, com marcação de tempo).

Uso:  python transcrever.py          (processa o que existe e fica esperando novos áudios; Ctrl+C sai)
      python transcrever.py --uma    (processa o que existe e termina)
      python transcrever.py --modelo medium   (mais preciso, bem mais lento; padrão: small)
"""
import argparse, glob, os, time
from faster_whisper import WhisperModel

RAIZ = r"D:\ESCOLA DE SEO - Conhecimento extraido"
AUDIOS = os.path.join(RAIZ, "05-AUDIOS")
SAIDA = os.path.join(RAIZ, "06-TRANSCRICOES")


def marca(s):
    return f"{int(s)//60:02d}:{int(s)%60:02d}"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--uma", action="store_true"); ap.add_argument("--modelo", default="small")
    a = ap.parse_args()
    os.makedirs(SAIDA, exist_ok=True)
    modelo = WhisperModel(a.modelo, device="cpu", compute_type="int8")
    while True:
        pendentes = [f for f in sorted(glob.glob(os.path.join(AUDIOS, "*.final.wav")))
                     if not os.path.exists(os.path.join(SAIDA, os.path.basename(f).replace(".final.wav", ".txt")))]
        for f in pendentes:
            nome = os.path.basename(f).replace(".final.wav", "")
            print(f"Transcrevendo {nome}...", flush=True)
            segs, _ = modelo.transcribe(f, language="pt", vad_filter=True, beam_size=5,
                                        initial_prompt="Aula sobre Google Meu Negócio, Perfil da Empresa, SEO local, GBPCheck, GPT, skill, palavras-chave.")
            with open(os.path.join(SAIDA, nome + ".txt"), "w", encoding="utf-8") as out:
                for s in segs:
                    out.write(f"[{marca(s.start)}] {s.text.strip()}\n")
            print(f"  pronto: {nome}.txt", flush=True)
        if a.uma: break
        time.sleep(20)
