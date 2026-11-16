#!/usr/bin/env python3
"""Flat SVG pictures for Unit 6 Jobs, viewBox 0 0 160 100."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
INK = "#233044"
SKY = "#BDE3FF"


def svg(body, bg=SKY):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 100" '
            f'role="img"><rect width="160" height="100" fill="{bg}"/>{body}</svg>')


def ground(c="#8ED081", y=78):
    return f'<rect y="{y}" width="160" height="{100-y}" fill="{c}"/>'


def firefighter():
    b = ground("#F6C177")
    b += ('<path d="M80 22 C92 38 97 45 97 56 a17 15 0 0 1 -34 0 C63 45 69 36 80 22Z" fill="#F4842B"/>'
          '<path d="M80 40 C87 50 89 54 89 59 a9 8 0 0 1 -18 0 C71 54 74 48 80 40Z" fill="#FFC53D"/>'
          '<path d="M46 82 a34 20 0 0 1 68 0 l0 6 H46 Z" fill="#FFC53D" stroke="#E8A33D" stroke-width="2.5"/>'
          '<rect x="58" y="66" width="44" height="9" rx="4" fill="#E4572E"/>')
    return svg(b)


def police():
    b = ground()
    b += ('<path d="M48 44 a32 18 0 0 1 64 0 l4 8 H44 Z" fill="#0052A4" stroke="' + INK + '" stroke-width="2.5"/>'
          '<path d="M40 54 h80 l6 8 H34 Z" fill="#233044"/>'
          '<path d="M80 58 l5 7 9 1 -3 8 4 7 -9 -2 -6 6 -6 -6 -9 2 4 -7 -3 -8 9 -1 Z" fill="#FFC53D" stroke="#E8A33D" stroke-width="2"/>')
    return svg(b)


def postman():
    b = ground()
    b += ('<rect x="36" y="30" width="88" height="46" rx="5" fill="#FFFFFF" stroke="' + INK + '" stroke-width="2.5"/>'
          '<path d="M38 33 L80 58 L122 33" fill="none" stroke="#E4572E" stroke-width="3"/>'
          '<rect x="102" y="36" width="14" height="11" rx="2" fill="#4FB3E8"/>'
          '<circle cx="80" cy="66" r="5" fill="#EF7C1C"/>')
    return svg(b)


def librarian():
    b = ground("#D9B98A")
    b += ('<path d="M28 26 h46 v52 H28 Z" fill="#FFFFFF"/>'
          '<path d="M28 26 q23 -10 46 0 v52 q-23 -10 -46 0 Z" fill="#FDF6E3" stroke="' + INK + '" stroke-width="2.5"/>'
          '<path d="M86 26 h46 v52 H86 Z" fill="#FFFFFF"/>'
          '<path d="M132 26 q-23 -10 -46 0 v52 q23 -10 46 0 Z" fill="#FDF6E3" stroke="' + INK + '" stroke-width="2.5"/>'
          '<path d="M36 38 h30 M36 48 h30 M36 58 h30 M94 38 h30 M94 48 h30 M94 58 h30" stroke="#9AA7B8" stroke-width="3" stroke-linecap="round"/>')
    return svg(b)


def cleaner():
    b = ground("#B8D8EA")
    b += ('<path d="M52 58 h44 l-5 26 a6 6 0 0 1 -6 5 H63 a6 6 0 0 1 -6 -5 Z" fill="#4FB3E8" stroke="' + INK + '" stroke-width="2.5"/>'
          '<path d="M52 58 q22 8 44 0" fill="none" stroke="' + INK + '" stroke-width="2.5"/>'
          '<line x1="98" y1="16" x2="80" y2="58" stroke="#8A5A33" stroke-width="4" stroke-linecap="round"/>'
          '<path d="M72 58 q8 10 16 0 l-2 10 q-6 6 -12 0 Z" fill="#F2C230"/>'
          '<circle cx="118" cy="34" r="5" fill="#FFFFFF" opacity="0.85"/><circle cx="128" cy="48" r="3.6" fill="#FFFFFF" opacity="0.85"/><circle cx="112" cy="52" r="3" fill="#FFFFFF" opacity="0.85"/>')
    return svg(b)


def architect():
    b = '<rect width="160" height="100" fill="#DCEEFF"/>'
    b += ('<rect x="30" y="18" width="100" height="64" rx="4" fill="#FFFFFF" stroke="#0052A4" stroke-width="2.5"/>'
          '<path d="M44 66 V44 l18 -12 18 12 v22 Z" fill="none" stroke="#0052A4" stroke-width="2.5"/>'
          '<rect x="56" y="52" width="10" height="14" fill="#BDE3FF" stroke="#0052A4" stroke-width="2"/>'
          '<path d="M88 40 h30 M88 50 h30 M88 60 h22" stroke="#9AA7B8" stroke-width="3" stroke-linecap="round"/>'
          '<line x1="102" y1="86" x2="126" y2="62" stroke="#EF7C1C" stroke-width="5" stroke-linecap="round"/>'
          '<path d="M126 62 l6 -2 -2 6 Z" fill="#233044"/>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 100" role="img">' + b + '</svg>')


def programmer():
    b = ground("#3A4767")
    b += ('<rect x="38" y="24" width="84" height="52" rx="6" fill="#233044"/>'
          '<rect x="45" y="31" width="70" height="38" rx="3" fill="#BDE3FF"/>'
          '<text x="80" y="58" font-size="19" font-family="monospace" font-weight="bold" fill="#0052A4" text-anchor="middle">&lt;/&gt;</text>'
          '<path d="M30 82 h100 l6 8 H24 Z" fill="#5B6B80"/>')
    return svg(b, "#2E3A5C")


def scientist():
    b = ground("#D8F3DC")
    b += ('<path d="M70 14 h20 M75 14 v18 l-16 30 a8 8 0 0 0 7 12 h28 a8 8 0 0 0 7 -12 L85 32 V14" fill="#EAF6FF" stroke="' + INK + '" stroke-width="2.5" stroke-linejoin="round"/>'
          '<path d="M64 56 h32 l5 9 a8 8 0 0 1 -7 9 H66 a8 8 0 0 1 -7 -9 Z" fill="#00A84D" opacity="0.8"/>'
          '<circle cx="74" cy="62" r="3" fill="#FFFFFF"/><circle cx="86" cy="52" r="2.4" fill="#FFFFFF"/><circle cx="80" cy="68" r="2" fill="#FFFFFF"/>'
          '<circle cx="112" cy="30" r="4" fill="#996CAC" opacity="0.7"/><circle cx="122" cy="44" r="3" fill="#996CAC" opacity="0.7"/>')
    return svg(b)


def hairdresser():
    b = ground("#FCE4EC")
    b += ('<g stroke="' + INK + '" stroke-width="3" stroke-linecap="round">'
          '<line x1="52" y1="30" x2="96" y2="66"/><line x1="52" y1="66" x2="96" y2="30"/></g>'
          '<circle cx="46" cy="72" r="7" fill="none" stroke="' + INK + '" stroke-width="3"/>'
          '<circle cx="46" cy="24" r="7" fill="none" stroke="' + INK + '" stroke-width="3"/>'
          '<path d="M112 26 v44 M106 26 h12 M107 36 h10 M107 46 h10 M107 56 h10 M108 70 h8" stroke="#E4572E" stroke-width="3.4" stroke-linecap="round"/>')
    return svg(b)


def publisher():
    b = ground("#D9B98A")
    b += ('<rect x="44" y="52" width="52" height="13" rx="3" fill="#E4572E"/>'
          '<rect x="48" y="39" width="52" height="13" rx="3" fill="#0052A4"/>'
          '<rect x="44" y="26" width="52" height="13" rx="3" fill="#00A84D"/>'
          '<path d="M50 32 h34 M54 45 h34 M50 58 h34" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.8"/>'
          '<path d="M104 22 h30 v40 h-30 Z" fill="#FFFFFF" stroke="' + INK + '" stroke-width="2.5"/>'
          '<path d="M109 30 h20 M109 38 h20 M109 46 h14" stroke="#9AA7B8" stroke-width="3" stroke-linecap="round"/>')
    return svg(b)


def pilot():
    b = ('<circle cx="28" cy="20" r="9" fill="#FFE9A8"/>'
         '<path d="M14 66 q10 -6 20 0 t20 0" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity="0.9"/>'
         '<path d="M104 26 q10 -6 20 0 t20 0" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity="0.9"/>')
    b += ('<path d="M18 56 L66 40 L62 30 L78 26 L96 38 L142 30 L146 38 L102 52 L104 64 L96 66 L88 56 L34 68 Z" fill="#FFFFFF" stroke="' + INK + '" stroke-width="2.5" stroke-linejoin="round"/>'
          '<path d="M96 38 L112 34 M84 44 l8 -2" stroke="#4FB3E8" stroke-width="3.4" stroke-linecap="round"/>')
    return svg(b)


def sailor():
    b = '<rect y="62" width="160" height="38" fill="#4FB3E8"/>'
    b += ('<path d="M0 70 q10 -5 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#BDE3FF" stroke-width="3"/>'
          '<rect x="76" y="16" width="5" height="38" fill="#8A5A33"/>'
          '<path d="M81 18 L112 48 L81 48 Z" fill="#FFFFFF" stroke="' + INK + '" stroke-width="2"/>'
          '<path d="M76 24 L56 48 L76 48 Z" fill="#EF7C1C"/>'
          '<path d="M40 54 h84 l-10 14 H52 Z" fill="#E4572E" stroke="' + INK + '" stroke-width="2.5" stroke-linejoin="round"/>')
    return svg(b)


def musician():
    b = ground("#F6C177")
    b += ('<path d="M66 22 a10 10 0 0 1 14 14 l22 22 a13 13 0 0 1 -18 18 L62 54 a10 10 0 0 1 -6 -16 Z" fill="#B5651D" stroke="' + INK + '" stroke-width="2.5"/>'
          '<circle cx="82" cy="60" r="9" fill="#5B3A17"/>'
          '<rect x="94" y="12" width="26" height="9" rx="3" fill="#233044" transform="rotate(38 107 16)"/>'
          '<path d="M40 30 q4 -8 10 -4 v14 M40 30 v16 a6 5 0 1 1 -4 -8" fill="none" stroke="#996CAC" stroke-width="3" stroke-linecap="round"/>'
          '<path d="M126 56 q4 -8 10 -4 v14 M126 56 v16 a6 5 0 1 1 -4 -8" fill="none" stroke="#0052A4" stroke-width="3" stroke-linecap="round"/>')
    return svg(b)


def politician():
    b = ground("#B8D8EA")
    b += ('<rect x="52" y="58" width="56" height="24" rx="4" fill="#0052A4" stroke="' + INK + '" stroke-width="2.5"/>'
          '<circle cx="80" cy="70" r="6" fill="#FFC53D"/>'
          '<line x1="80" y1="58" x2="66" y2="30" stroke="' + INK + '" stroke-width="3.4" stroke-linecap="round"/>'
          '<circle cx="64" cy="27" r="6" fill="#233044"/>'
          '<line x1="80" y1="58" x2="96" y2="34" stroke="' + INK + '" stroke-width="3.4" stroke-linecap="round"/>'
          '<rect x="93" y="26" width="13" height="10" rx="4" fill="#5B6B80" transform="rotate(24 99 31)"/>')
    return svg(b)


IMGS = {
    "c1-firefighter.svg": firefighter(),
    "c2-police.svg": police(),
    "c3-postman.svg": postman(),
    "c4-librarian.svg": librarian(),
    "c5-cleaner.svg": cleaner(),
    "c6-architect.svg": architect(),
    "c7-programmer.svg": programmer(),
    "c8-scientist.svg": scientist(),
    "c9-hairdresser.svg": hairdresser(),
    "c10-publisher.svg": publisher(),
    "c11-pilot.svg": pilot(),
    "c12-sailor.svg": sailor(),
    "c13-musician.svg": musician(),
    "c14-politician.svg": politician(),
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, body in IMGS.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(body)
    print("drew", len(IMGS), "images")
