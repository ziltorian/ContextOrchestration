#!/usr/bin/env python3
"""
WCAG contrast ratio checker.
Usage: python check-contrast.py "#111111" "#ffffff"
       python check-contrast.py "18,18,18" "255,255,255"

Returns the contrast ratio and WCAG AA/AAA pass/fail status.
"""

import sys
import re


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def parse_color(color: str) -> tuple[int, int, int]:
    color = color.strip()
    if color.startswith("#"):
        return hex_to_rgb(color)
    # Try "r,g,b" format
    parts = re.split(r"[,\s]+", color)
    if len(parts) == 3:
        return tuple(int(p) for p in parts)
    raise ValueError(f"Cannot parse color: {color!r}")


def relative_luminance(r: int, g: int, b: int) -> float:
    """WCAG relative luminance — IEC 61966-2-1"""
    def linearize(c: int) -> float:
        s = c / 255
        return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4

    return 0.2126 * linearize(r) + 0.7152 * linearize(g) + 0.0722 * linearize(b)


def contrast_ratio(fg: tuple, bg: tuple) -> float:
    l1 = relative_luminance(*fg)
    l2 = relative_luminance(*bg)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def check(foreground: str, background: str, font_size_pt: float = 12, bold: bool = False):
    fg = parse_color(foreground)
    bg = parse_color(background)
    ratio = contrast_ratio(fg, bg)

    large_text = font_size_pt >= 18 or (font_size_pt >= 14 and bold)
    aa_threshold  = 3.0 if large_text else 4.5
    aaa_threshold = 4.5 if large_text else 7.0

    aa_pass  = ratio >= aa_threshold
    aaa_pass = ratio >= aaa_threshold
    ui_pass  = ratio >= 3.0  # UI components threshold

    print(f"\nContrast: {foreground!r} on {background!r}")
    print(f"  Ratio:       {ratio:.2f}:1")
    print(f"  Text size:   {'large' if large_text else 'normal'}")
    print(f"  WCAG AA:     {'✅ PASS' if aa_pass else '❌ FAIL'} (threshold {aa_threshold}:1)")
    print(f"  WCAG AAA:    {'✅ PASS' if aaa_pass else '❌ FAIL'} (threshold {aaa_threshold}:1)")
    print(f"  UI Components: {'✅ PASS' if ui_pass else '❌ FAIL'} (threshold 3:1)")
    return ratio


def batch_check(pairs: list[tuple[str, str]]):
    """Check a list of (foreground, background) color pairs."""
    results = []
    for fg, bg in pairs:
        fg_rgb = parse_color(fg)
        bg_rgb = parse_color(bg)
        ratio = contrast_ratio(fg_rgb, bg_rgb)
        aa = ratio >= 4.5
        results.append((fg, bg, ratio, aa))

    print(f"\n{'Foreground':<20} {'Background':<20} {'Ratio':>8}  AA")
    print("-" * 58)
    for fg, bg, ratio, aa in sorted(results, key=lambda x: x[2]):
        status = "✅" if aa else "❌"
        print(f"{fg:<20} {bg:<20} {ratio:>6.2f}:1  {status}")


# Common desktop palette check
DESKTOP_PALETTE_CHECK = [
    # (foreground, background)
    ("#111111", "#ffffff"),       # primary text on white
    ("#52525b", "#ffffff"),       # secondary text on white
    ("#71717a", "#ffffff"),       # tertiary text on white — borderline
    ("#a1a1aa", "#ffffff"),       # disabled on white — expect fail
    ("#ffffff", "#18181b"),       # white on near-black
    ("#e4e4e7", "#18181b"),       # light text on dark
    ("#a1a1aa", "#18181b"),       # secondary on dark
    ("#71717a", "#18181b"),       # tertiary on dark — check
    ("#ffffff", "#2563eb"),       # white on blue action
    ("#ffffff", "#16a34a"),       # white on green success
    ("#ffffff", "#dc2626"),       # white on red error
]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Running common desktop palette check…")
        batch_check(DESKTOP_PALETTE_CHECK)
    elif len(sys.argv) >= 3:
        fg_arg = sys.argv[1]
        bg_arg = sys.argv[2]
        size = float(sys.argv[3]) if len(sys.argv) > 3 else 12
        bold = "--bold" in sys.argv
        check(fg_arg, bg_arg, size, bold)
    else:
        print("Usage:")
        print("  python check-contrast.py                     # run palette check")
        print("  python check-contrast.py '#111' '#fff'        # check two colors")
        print("  python check-contrast.py '#111' '#fff' 18     # large text (18pt)")
        print("  python check-contrast.py '#111' '#fff' 14 --bold  # 14pt bold = large")
