#!/usr/bin/env python3
"""Selo da serie 'Frase de Cliente' — faixa de assinatura, identica em todos os
episodios, posicionada na FAIXA VISIVEL DO GRID (y 1536-1636 do canvas 1080x1920).

Por que aqui: o grid do Instagram recorta o 4:5 central (y 285-1635). A faixa
inferior de marca comeca em 1536, entao a fatia 1536-1636 e o unico pedaco dela
que aparece na miniatura do perfil. Uma barra verde solida nessa faixa vira a
assinatura da serie: 10 posts com a mesma listra no mesmo lugar.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 100          # faixa cheia
ACCENT = (0, 198, 109, 255)      # --landing-accent #00C66D
INK = (7, 32, 20, 255)           # --landing-dark #072014

FONT_BOLD = "/root/.fonts/Inter-Bold.ttf"
FONT_BLACK = "/root/.fonts/Inter-Black.ttf"


def load(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def build(ep: int, total: int, out: str):
    im = Image.new("RGBA", (W, H), ACCENT)
    d = ImageDraw.Draw(im)

    nome = "FRASE DE CLIENTE"
    ep_txt = f"EP {ep:02d}/{total}"

    f_nome = load(FONT_BOLD, 46)
    f_ep = load(FONT_BLACK, 46)

    # tracking manual no nome (letterspacing do kicker do kit: +0.16em)
    track = 7
    largura_nome = sum(d.textlength(c, font=f_nome) + track for c in nome) - track
    largura_ep = d.textlength(ep_txt, font=f_ep)
    sep_w = 46  # espaco do separador " · "

    total_w = largura_nome + sep_w + largura_ep
    x = (W - total_w) / 2
    y = (H - 52) / 2

    for c in nome:
        d.text((x, y), c, font=f_nome, fill=INK)
        x += d.textlength(c, font=f_nome) + track

    # ponto separador
    cx = x + sep_w / 2 - track
    d.ellipse([cx - 7, H / 2 - 7, cx + 7, H / 2 + 7], fill=INK)

    d.text((x + sep_w - track, y), ep_txt, font=f_ep, fill=INK)

    im.save(out)
    print(f"selo ep{ep:02d} -> {out}")


if __name__ == "__main__":
    total = 10
    for ep in range(1, total + 1):
        build(ep, total, f"/home/claude/serie/selo-{ep:02d}.png")
