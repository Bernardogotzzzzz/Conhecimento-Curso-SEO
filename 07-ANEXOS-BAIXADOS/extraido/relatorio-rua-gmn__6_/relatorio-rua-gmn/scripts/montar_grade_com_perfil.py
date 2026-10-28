#!/usr/bin/env python3
"""
Monta a imagem principal do relatorio de rua: a grade do prospect com o cartao
do perfil do Google colado por cima da area vazia do mapa.

Uso:
    python montar_grade_com_perfil.py grade.png perfil.png saida.jpg
    python montar_grade_com_perfil.py grade.png perfil.png saida.jpg --lado esquerda
    python montar_grade_com_perfil.py grade.png perfil.png saida.jpg --x 0.60 --y 0.09 --altura 0.78

Parametros opcionais:
    --lado     direita (padrao) ou esquerda. So define o lado padrao do encaixe.
    --x        posicao horizontal do cartao, de 0 a 1 da largura da grade.
    --y        posicao vertical do cartao, de 0 a 1 da altura da grade.
    --altura   altura do cartao, de 0 a 1 da altura da grade. Padrao 0.79.
    --escala   fator de ampliacao antes de compor, para nao perder nitidez. Padrao 2.

O script avisa se o cartao estourar a borda da grade, em vez de cortar calado.
"""
import argparse
import sys

from PIL import Image, ImageDraw, ImageFilter

BORDA = (220, 227, 236, 255)
SOMBRA = (3, 18, 47, 110)


def montar(grade_path, perfil_path, saida_path, lado="direita",
           x=None, y=0.10, altura=0.79, escala=2):
    grade = Image.open(grade_path).convert("RGB")
    perfil = Image.open(perfil_path).convert("RGB")

    if escala > 1:
        grade = grade.resize((grade.width * escala, grade.height * escala), Image.LANCZOS)
    W, H = grade.size

    alt_perfil = int(H * altura)
    r = alt_perfil / perfil.height
    perfil = perfil.resize((max(1, int(perfil.width * r)), alt_perfil), Image.LANCZOS)

    pad = max(6, int(H * 0.011))
    card_w, card_h = perfil.width + pad * 2, perfil.height + pad * 2
    raio = max(8, int(H * 0.015))

    if x is None:
        x = 0.56 if lado == "direita" else 0.02
    px, py = int(W * x), int(H * y)

    if px + card_w > W or py + card_h > H:
        print("AVISO: o cartao do perfil nao cabe nessa posicao.", file=sys.stderr)
        print(f"  grade {W}x{H}, cartao {card_w}x{card_h} em ({px},{py}).", file=sys.stderr)
        print("  Reduza --altura ou ajuste --x e --y.", file=sys.stderr)
        sys.exit(1)

    base = grade.convert("RGBA")

    sombra = Image.new("RGBA", (card_w + 40, card_h + 40), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rounded_rectangle(
        [20, 22, 20 + card_w, 22 + card_h], radius=raio, fill=SOMBRA)
    sombra = sombra.filter(ImageFilter.GaussianBlur(11))
    base.alpha_composite(sombra, (px - 20, py - 20))

    card = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle(
        [0, 0, card_w - 1, card_h - 1], radius=raio,
        fill=(255, 255, 255, 255), outline=BORDA, width=2)
    card.paste(perfil, (pad, pad))

    mascara = Image.new("L", (card_w, card_h), 0)
    ImageDraw.Draw(mascara).rounded_rectangle(
        [0, 0, card_w - 1, card_h - 1], radius=raio, fill=255)
    base.paste(card, (px, py), mascara)

    final = base.convert("RGB")
    if saida_path.lower().endswith((".jpg", ".jpeg")):
        final.save(saida_path, "JPEG", quality=90)
    else:
        final.save(saida_path)
    print("montagem gerada:", saida_path, final.size)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("grade")
    ap.add_argument("perfil")
    ap.add_argument("saida")
    ap.add_argument("--lado", choices=["direita", "esquerda"], default="direita")
    ap.add_argument("--x", type=float, default=None)
    ap.add_argument("--y", type=float, default=0.10)
    ap.add_argument("--altura", type=float, default=0.79)
    ap.add_argument("--escala", type=int, default=2)
    a = ap.parse_args()
    montar(a.grade, a.perfil, a.saida, a.lado, a.x, a.y, a.altura, a.escala)
