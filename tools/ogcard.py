#!/usr/bin/env python3
"""The social card, generated from the packs themselves — stdlib only, no rasterizer.

A link to the catalogue rendered as an empty box: every page declared `twitter:card`
and shipped no image, which is an unbacked claim in the one place a shared link is
meant to work.

The card carries no text on purpose. It is a grid of every pack's real field, ink and
accent, read out of `styles/tokens/<pack>.css` — so the picture of the catalogue IS the
catalogue, and it cannot drift from it. The words come from `og:title`, which the
platform renders itself.

A PNG is three chunks and a CRC; `zlib.compress` does the rest.
"""
from __future__ import annotations

import struct
import zlib

W, H = 1200, 630


def _chunk(tag: bytes, data: bytes) -> bytes:
    return (struct.pack(">I", len(data)) + tag + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))


def encode_png(pixels: bytearray, width: int = W, height: int = H) -> bytes:
    """`pixels` is width*height*3 bytes, RGB. Truecolour, 8-bit, filter 0 — the
    simplest thing every decoder is required to accept."""
    raw = bytearray()
    stride = width * 3
    for y in range(height):
        raw.append(0)                      # filter: none
        raw += pixels[y * stride:(y + 1) * stride]
    return (b"\x89PNG\r\n\x1a\n"
            + _chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
            + _chunk(b"IDAT", zlib.compress(bytes(raw), 9))
            + _chunk(b"IEND", b""))


def _rgb(value: str, fallback=(255, 255, 255)) -> tuple[int, int, int]:
    v = (value or "").strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if len(v) != 6:
        return fallback
    try:
        return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]
    except ValueError:
        return fallback


def card(packs: list[dict]) -> bytes:
    """One cell per pack: its field, a band of its ink, and a mark in its accent."""
    if not packs:
        raise ValueError("no packs — a card that shows nothing is worse than no card")
    cols = 7
    rows = -(-len(packs) // cols)
    cw, ch = W // cols, H // rows
    px = bytearray(b"\x00" * (W * H * 3))

    def fill(x0: int, y0: int, x1: int, y1: int, rgb: tuple[int, int, int]) -> None:
        x0, y0 = max(0, x0), max(0, y0)
        x1, y1 = min(W, x1), min(H, y1)
        row = bytes(rgb) * (x1 - x0)
        for y in range(y0, y1):
            off = (y * W + x0) * 3
            px[off:off + len(row)] = row

    for i, p in enumerate(packs):
        cx, cy = (i % cols) * cw, (i // cols) * ch
        field = _rgb(p.get("bg"))
        ink = _rgb(p.get("ink"), (0, 0, 0))
        accent = _rgb(p.get("accent"), ink)
        # Three strips, because a card is read at thumbnail size: the field takes most
        # of the cell, then the ink, then the accent. A square floating in a field
        # reads as monotony once the image is 300px wide; three bands read as a swatch.
        a = cx + int(cw * 0.62)
        b = cx + int(cw * 0.81)
        fill(cx, cy, a, cy + ch, field)
        fill(a, cy, b, cy + ch, ink)
        fill(b, cy, cx + cw, cy + ch, accent)
        # a hairline in the ink so two white fields side by side stay two
        fill(cx, cy, cx + cw, cy + 1, ink)
        fill(cx, cy, cx + 1, cy + ch, ink)
    return encode_png(px)
