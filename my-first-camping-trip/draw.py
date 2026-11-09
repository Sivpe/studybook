#!/usr/bin/env python3
"""Flat SVG pictures for My First Camping Trip, viewBox 0 0 160 100."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
INK = "#233044"
DAY = "#BDE3FF"
NIGHT = "#2E3A5C"


def base(bg, ground="#8ED081", gy=74):
    return (f'<rect width="160" height="100" fill="{bg}"/>'
            f'<rect y="{gy}" width="160" height="{100-gy}" fill="{ground}"/>')


def star(x, y, s=3, c="#FFE066"):
    return (f'<path d="M{x} {y-s} L{x+s*0.35} {y-s*0.35} L{x+s} {y} L{x+s*0.35} {y+s*0.35} '
            f'L{x} {y+s} L{x-s*0.35} {y+s*0.35} L{x-s} {y} L{x-s*0.35} {y-s*0.35} Z" fill="{c}"/>')


def moon(x=132, y=20):
    return f'<circle cx="{x}" cy="{y}" r="10" fill="#FFE9A8"/><circle cx="{x-5}" cy="{y-3}" r="8" fill="{NIGHT}"/>'


def tree(x, y, s=1.0, dark="#2E7D4F"):
    return (f'<rect x="{x-2*s}" y="{y-16*s}" width="{4*s}" height="{16*s}" fill="#8A5A33"/>'
            f'<path d="M{x} {y-44*s} L{x+13*s} {y-14*s} L{x-13*s} {y-14*s} Z" fill="{dark}"/>')


def svg(body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 100" '
            f'role="img">{body}</svg>')


def backpack():
    b = base(DAY)
    b += (f'<rect x="56" y="26" width="48" height="52" rx="14" fill="#EF7C1C" stroke="{INK}" stroke-width="2.5"/>'
          f'<path d="M64 28 a16 10 0 0 1 32 0" fill="none" stroke="{INK}" stroke-width="2.5"/>'
          f'<rect x="64" y="48" width="32" height="22" rx="6" fill="#FFC53D" stroke="{INK}" stroke-width="2.5"/>'
          f'<rect x="72" y="36" width="16" height="7" rx="3.5" fill="#0052A4"/>')
    return svg(b)


def swim():
    b = f'<rect width="160" height="100" fill="{DAY}"/>'
    b += '<rect y="52" width="160" height="48" fill="#4FB3E8"/>'
    b += ('<path d="M0 62 q10 -5 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#BDE3FF" stroke-width="3"/>'
          '<path d="M0 84 q10 -5 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#BDE3FF" stroke-width="3"/>')
    ring = ('<g transform="rotate(-12 80 52)"><ellipse cx="80" cy="52" rx="30" ry="13" fill="#E4572E"/>'
            '<ellipse cx="80" cy="52" rx="14" ry="5.5" fill="#4FB3E8"/>'
            '<path d="M56 46 a30 13 0 0 1 12 -7 l3 9 a14 5.5 0 0 0 -8 3 Z" fill="#FFFFFF" opacity="0.85"/>'
            '<path d="M92 39 a30 13 0 0 1 12 7 l-11 2 a14 5.5 0 0 0 -4 -6 Z" fill="#FFFFFF" opacity="0.85"/></g>')
    b += ring
    return svg(b)


def bus():
    b = base(NIGHT, "#3A4767", 78)
    b += moon(24, 18) + star(52, 14) + star(120, 12, 2.4)
    b += (f'<rect x="34" y="26" width="92" height="52" rx="9" fill="#FFC53D" stroke="{INK}" stroke-width="2.5"/>'
          f'<rect x="42" y="33" width="34" height="18" rx="3" fill="#BDE3FF" stroke="{INK}" stroke-width="2"/>'
          f'<rect x="84" y="33" width="34" height="18" rx="3" fill="#BDE3FF" stroke="{INK}" stroke-width="2"/>'
          '<circle cx="50" cy="62" r="5" fill="#FFF6C9" stroke="#E8A33D" stroke-width="2"/>'
          '<circle cx="110" cy="62" r="5" fill="#FFF6C9" stroke="#E8A33D" stroke-width="2"/>'
          '<path d="M38 66 L18 74 M122 66 L142 74" stroke="#FFF6C9" stroke-width="3" stroke-linecap="round" opacity="0.7"/>'
          f'<circle cx="56" cy="80" r="8" fill="{INK}"/><circle cx="104" cy="80" r="8" fill="{INK}"/>')
    return svg(b)


def tent():
    b = base(NIGHT, "#3A4767", 76)
    b += moon() + star(30, 16) + star(62, 10, 2.4) + star(100, 26, 2.2)
    b += tree(18, 78, 0.9, "#274434") + tree(146, 78, 0.8, "#274434")
    b += (f'<path d="M80 30 L118 76 L42 76 Z" fill="#EF7C1C" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>'
          f'<path d="M80 46 L94 76 L66 76 Z" fill="#7A3B12"/>'
          f'<path d="M80 30 L80 46" stroke="{INK}" stroke-width="2.5"/>')
    return svg(b)


def poles():
    b = base(DAY)
    for i, dx in enumerate([-14, -5, 4, 13]):
        b += (f'<line x1="{80+dx-8}" y1="86" x2="{80+dx+10}" y2="18" stroke="#9AA7B8" stroke-width="5" stroke-linecap="round"/>'
              f'<circle cx="{80+dx+10}" cy="18" r="3.4" fill="#5B6B80"/>')
    b += f'<rect x="52" y="58" width="56" height="7" rx="3.5" fill="#E4572E" transform="rotate(-64 80 62)"/>'
    return svg(b)


def stars():
    b = f'<rect width="160" height="100" fill="{NIGHT}"/>'
    b += moon(34, 24)
    pts = [(70, 14), (96, 22), (124, 12), (146, 30), (58, 34), (112, 40), (84, 48), (140, 52), (26, 56), (66, 66)]
    for i, (x, y) in enumerate(pts):
        b += star(x, y, 3.4 if i % 3 == 0 else 2.4)
    b += '<rect y="84" width="160" height="16" fill="#3A4767"/>'
    b += f'<path d="M28 84 L46 66 L64 84 Z" fill="#EF7C1C"/><path d="M104 84 L120 70 L136 84 Z" fill="#EF7C1C" opacity="0.75"/>'
    return svg(b)


def campfire():
    b = base(NIGHT, "#3A4767", 78)
    b += star(24, 14) + star(140, 18, 2.4)
    b += ('<rect x="52" y="70" width="56" height="9" rx="4.5" fill="#8A5A33" transform="rotate(9 80 74)"/>'
          '<rect x="52" y="70" width="56" height="9" rx="4.5" fill="#A9713F" transform="rotate(-9 80 74)"/>'
          '<path d="M80 26 C92 44 96 52 96 62 a16 14 0 0 1 -32 0 C64 52 70 42 80 26Z" fill="#F4842B"/>'
          '<path d="M80 44 C87 54 89 58 89 63 a9 8 0 0 1 -18 0 C71 58 74 52 80 44Z" fill="#FFC53D"/>'
          f'<line x1="112" y1="34" x2="94" y2="56" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>'
          '<rect x="106" y="26" width="13" height="10" rx="4" fill="#FFFFFF" stroke="#E8A33D" stroke-width="2"/>')
    return svg(b)


def sock():
    b = base(DAY)
    sock_path = "M62 22 h22 v26 q0 4 4 7 l10 9 a10 10 0 0 1 -13 15 l-20 -14 a14 14 0 0 1 -3 -11 Z"
    b += f'<path d="{sock_path}" fill="none" stroke="#9AA7B8" stroke-width="2.5" stroke-dasharray="5 4" opacity="0.65" transform="translate(26 6)"/>'
    b += (f'<path d="M34 18 h22 v26 q0 4 4 7 l10 9 a10 10 0 0 1 -13 15 L37 61 a14 14 0 0 1 -3 -11 Z" fill="#996CAC" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>'
          '<path d="M34 30 h22 M36 56 l20 13" stroke="#FFFFFF" stroke-width="4" opacity="0.55"/>')
    b += f'<text x="118" y="34" font-size="20" fill="#E4572E" font-family="sans-serif" font-weight="bold">?</text>'
    return svg(b)


def fishing():
    b = f'<rect width="160" height="100" fill="{DAY}"/>'
    b += '<rect y="64" width="160" height="36" fill="#4FB3E8"/>'
    b += ('<path d="M14 78 q8 -4 16 0 t16 0 t16 0" fill="none" stroke="#BDE3FF" stroke-width="3"/>'
          f'<line x1="18" y1="12" x2="96" y2="52" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>'
          '<path d="M96 52 L96 68" stroke="#FFFFFF" stroke-width="1.8"/>'
          '<path d="M96 68 q5 5 0 9" fill="none" stroke="#5B6B80" stroke-width="2.5"/>'
          '<path d="M104 82 q12 -10 24 0 q-12 10 -24 0Z" fill="#EF7C1C"/>'
          '<path d="M128 82 l10 -6 v12 Z" fill="#E4572E"/><circle cx="110" cy="80" r="2" fill="#233044"/>')
    b += '<rect y="88" width="160" height="12" fill="#3E9BD6"/>'
    return svg(b)


def straw_path():
    b = base(DAY)
    b += tree(16, 74, 1.1) + tree(40, 70, 0.85) + tree(124, 70, 0.9) + tree(148, 76, 1.15)
    b += '<path d="M66 100 L76 62 L88 62 L100 100 Z" fill="#D9B98A"/>'
    for (x, y, r) in [(72, 88, -18), (88, 80, 14), (78, 70, -8), (92, 94, 20), (66, 78, 10)]:
        b += f'<line x1="{x-7}" y1="{y}" x2="{x+7}" y2="{y}" stroke="#F2C230" stroke-width="3.4" stroke-linecap="round" transform="rotate({r} {x} {y})"/>'
    return svg(b)


def bag_poles():
    b = base(DAY)
    for dx in (-8, 2, 12):
        b += f'<line x1="{80+dx}" y1="52" x2="{80+dx-6}" y2="16" stroke="#9AA7B8" stroke-width="5" stroke-linecap="round"/>'
    b += (f'<path d="M46 56 q34 -12 68 0 l-5 26 a8 8 0 0 1 -8 6 H59 a8 8 0 0 1 -8 -6 Z" fill="#00A84D" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>'
          f'<path d="M46 56 q34 10 68 0" fill="none" stroke="{INK}" stroke-width="2.5"/>'
          '<rect x="70" y="66" width="20" height="12" rx="3" fill="#FFC53D"/>')
    return svg(b)


def scarecrow():
    b = base(DAY, "#F2D06B", 72)
    b += tree(14, 74, 0.9) + tree(148, 74, 0.9)
    b += (f'<rect x="77" y="34" width="6" height="52" fill="#8A5A33"/>'
          f'<line x1="52" y1="48" x2="108" y2="48" stroke="#8A5A33" stroke-width="5" stroke-linecap="round"/>'
          '<path d="M62 44 h36 l4 22 H58 Z" fill="#0052A4"/>'
          '<path d="M66 86 l5 -20 h6 v20 Z M84 86 l-4 -20 h7 l4 20 Z" fill="#7A4A21"/>'
          '<circle cx="80" cy="30" r="11" fill="#F2C230"/>'
          '<path d="M64 26 q16 -12 32 0 l-3 5 H67 Z" fill="#E4572E"/>'
          '<path d="M52 48 l-7 4 M108 48 l7 4 M62 66 l-6 5 M98 66 l6 5" stroke="#F2C230" stroke-width="3.4" stroke-linecap="round"/>'
          '<circle cx="76" cy="29" r="1.8" fill="#233044"/><circle cx="84" cy="29" r="1.8" fill="#233044"/>'
          '<path d="M75 35 q5 3 10 0" fill="none" stroke="#233044" stroke-width="1.8"/>')
    return svg(b)


IMGS = {
    "c1-bags.svg": backpack(),
    "c2-swim.svg": swim(),
    "c3-bus.svg": bus(),
    "c4-tent.svg": tent(),
    "c5-poles.svg": poles(),
    "c6-stars.svg": stars(),
    "c7-campfire.svg": campfire(),
    "c8-sock.svg": sock(),
    "c9-fishing.svg": fishing(),
    "c10-straw.svg": straw_path(),
    "c11-bag.svg": bag_poles(),
    "c12-scarecrow.svg": scarecrow(),
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, body in IMGS.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(body)
    print("drew", len(IMGS), "images")
