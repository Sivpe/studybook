# -*- coding: utf-8 -*-
"""Flat 2D object drawings for Power Up 6 Unit 5 school words.
Hand-authored SVG, viewBox 0 0 160 100, stroke grey #C9CED8 everywhere.
Run: python power-up-6-unit-5-school-words/draw.py"""
import io
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
NAVY, INK, WHITE, LINE = '#1C2A4A', '#23262D', '#FFFFFF', '#C9CED8'
BLUE, GREEN, ORANGE, YELLOW, RED = '#0052A4', '#00A84D', '#EF7C1C', '#F5B700', '#D7372B'
PALE = '#EEF0F4'


def svg(name, body):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 100">{body}</svg>\n'
    io.open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n').write(s)


os.makedirs(OUT, exist_ok=True)

# c1 course: open book
svg('c1-book.svg',
    f'<path d="M80 24 Q56 14 26 20 V82 Q56 76 80 86Z" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M80 24 Q104 14 134 20 V82 Q104 76 80 86Z" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M80 24 V86" stroke="{BLUE}" stroke-width="2.5"/>'
    + ''.join(f'<path d="M34 {34 + i * 11} Q54 {30 + i * 11} 72 {35 + i * 11}" stroke="{LINE}" stroke-width="2" fill="none"/>' for i in range(4))
    + ''.join(f'<path d="M88 {35 + i * 11} Q106 {30 + i * 11} 126 {34 + i * 11}" stroke="{LINE}" stroke-width="2" fill="none"/>' for i in range(4))
    + f'<path d="M34 34 Q54 30 72 35" stroke="{BLUE}" stroke-width="2.4" fill="none"/>')

# c2 level: steps going up with a flag
svg('c2-level.svg',
    f'<rect x="18" y="72" width="34" height="18" fill="{BLUE}"/>'
    f'<rect x="52" y="54" width="34" height="36" fill="{GREEN}"/>'
    f'<rect x="86" y="36" width="34" height="54" fill="{ORANGE}"/>'
    f'<rect x="118" y="10" width="4" height="34" fill="{INK}"/>'
    f'<path d="M122 10 H146 L140 18 L146 26 H122Z" fill="{YELLOW}"/>'
    f'<path d="M26 64 l10 -8 M60 46 l10 -8 M94 28 l10 -8" stroke="{WHITE}" stroke-width="3" stroke-linecap="round"/>')

# c3 term: calendar
svg('c3-calendar.svg',
    f'<rect x="38" y="12" width="84" height="80" rx="8" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<path d="M38 20 A8 8 0 0 1 46 12 H114 A8 8 0 0 1 122 20 V32 H38Z" fill="{BLUE}"/>'
    f'<rect x="56" y="6" width="6" height="14" rx="3" fill="{NAVY}"/><rect x="98" y="6" width="6" height="14" rx="3" fill="{NAVY}"/>'
    + ''.join(f'<rect x="{48 + (i % 3) * 23}" y="{44 + (i // 3) * 20}" width="17" height="15" rx="4" fill="{GREEN if i in (0, 1, 2) else PALE}"/>' for i in range(6)))

# c4 essay: page of writing with a pencil
svg('c4-essay.svg',
    f'<rect x="38" y="8" width="66" height="84" rx="4" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="48" y="18" width="34" height="6" rx="3" fill="{GREEN}"/>'
    + ''.join(f'<rect x="48" y="{34 + i * 11}" width="{46 if i % 2 == 0 else 38}" height="5" rx="2.5" fill="{LINE}"/>' for i in range(5))
    + f'<g transform="translate(118 58) rotate(-34)"><rect x="-5" y="-34" width="10" height="52" rx="3" fill="{YELLOW}"/>'
    f'<path d="M-5 18 L0 30 L5 18Z" fill="{INK}"/><rect x="-5" y="-34" width="10" height="10" rx="3" fill="{RED}"/></g>')

# c5 project: poster board with a chart and pictures
svg('c5-project.svg',
    f'<rect x="24" y="12" width="112" height="72" rx="5" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="24" y="12" width="112" height="14" rx="5" fill="{GREEN}"/>'
    f'<rect x="34" y="34" width="38" height="28" rx="3" fill="{PALE}" stroke="{LINE}" stroke-width="1.6"/>'
    f'<circle cx="46" cy="44" r="4.5" fill="{YELLOW}"/><path d="M36 62 L52 50 L60 56 L70 46 V62Z" fill="{GREEN}"/>'
    f'<rect x="82" y="58" width="9" height="16" fill="{BLUE}"/><rect x="95" y="50" width="9" height="24" fill="{ORANGE}"/><rect x="108" y="42" width="9" height="32" fill="{GREEN}"/>'
    f'<rect x="82" y="34" width="42" height="5" rx="2.5" fill="{LINE}"/>')

# c6 instructions: clipboard with a checklist
svg('c6-instructions.svg',
    f'<rect x="48" y="10" width="64" height="84" rx="6" fill="{NAVY}"/>'
    f'<rect x="54" y="18" width="52" height="70" rx="3" fill="{WHITE}"/>'
    f'<rect x="68" y="5" width="24" height="12" rx="4" fill="{LINE}"/>'
    + ''.join(
        f'<path d="M62 {32 + i * 17} l4 4 l7 -8" stroke="{GREEN}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
        f'<rect x="78" y="{30 + i * 17}" width="22" height="5" rx="2.5" fill="{LINE}"/>'
        for i in range(3)))

# c7 information: round information sign
svg('c7-information.svg',
    f'<circle cx="80" cy="46" r="34" fill="{BLUE}"/>'
    f'<circle cx="80" cy="46" r="34" fill="none" stroke="{LINE}" stroke-width="2"/>'
    f'<text x="80" y="66" font-family="Georgia, serif" font-size="52" font-weight="700" font-style="italic" fill="{WHITE}" text-anchor="middle">i</text>'
    f'<rect x="76" y="82" width="8" height="10" fill="{NAVY}"/>'
    f'<rect x="58" y="92" width="44" height="4" rx="2" fill="{LINE}"/>')

# c8 test: test paper with a clock
svg('c8-test.svg',
    f'<rect x="30" y="10" width="72" height="82" rx="4" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="40" y="19" width="40" height="6" rx="3" fill="{ORANGE}"/>'
    + ''.join(f'<rect x="40" y="{34 + i * 12}" width="{50 if i % 2 == 0 else 42}" height="5" rx="2.5" fill="{LINE}"/>' for i in range(4))
    + f'<circle cx="66" cy="76" r="4" fill="none" stroke="{GREEN}" stroke-width="2.4"/><path d="M62 76 l3 3 l6 -6" stroke="{GREEN}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    f'<circle cx="120" cy="66" r="20" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<circle cx="120" cy="66" r="17" fill="none" stroke="{ORANGE}" stroke-width="2"/>'
    f'<path d="M120 54 V66 L129 71" stroke="{INK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>')

# c9 mark: paper with a big top score
svg('c9-mark.svg',
    f'<rect x="42" y="8" width="76" height="84" rx="4" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    + ''.join(f'<rect x="52" y="{20 + i * 11}" width="40" height="5" rx="2.5" fill="{LINE}"/>' for i in range(3))
    + f'<text x="80" y="82" font-family="Georgia, serif" font-size="30" font-weight="700" fill="{RED}" text-anchor="middle">A+</text>'
    f'<path d="M56 86 Q80 92 104 86" stroke="{RED}" stroke-width="2.4" fill="none" stroke-linecap="round"/>')

# c10 certificate: certificate with a seal and ribbon
svg('c10-certificate.svg',
    f'<rect x="18" y="18" width="124" height="64" rx="4" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>'
    f'<rect x="24" y="24" width="112" height="52" rx="3" fill="none" stroke="{YELLOW}" stroke-width="2"/>'
    f'<rect x="52" y="32" width="56" height="6" rx="3" fill="{NAVY}"/>'
    + ''.join(f'<rect x="58" y="{46 + i * 9}" width="44" height="4.5" rx="2.2" fill="{LINE}"/>' for i in range(2))
    + f'<circle cx="118" cy="66" r="10" fill="{RED}"/>'
    f'<path d="M113 74 L109 90 L118 84 L127 90 L123 74Z" fill="{ORANGE}"/>'
    f'<circle cx="118" cy="66" r="5.5" fill="{YELLOW}"/>')
print('drawn:', sorted(os.listdir(OUT)))
