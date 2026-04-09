# Typography Reference

## Font Categories & Recommendations

### UI / System-Style (best for tool UIs, dashboards, settings)

| Font | Weight Range | Use Case | CDN |
|---|---|---|---|
| **Geist** | 100–900 | SaaS tools, developer apps | `https://vercel.com/font/geist` |
| **Outfit** | 100–900 | Clean SaaS, modern tools | Google Fonts |
| **DM Sans** | 100–900 | Neutral, versatile tool UI | Google Fonts |
| **Plus Jakarta Sans** | 200–800 | Polished products | Google Fonts |
| **IBM Plex Sans** | 100–700 | Data-dense, enterprise | Google Fonts |
| **Source Sans 3** | 200–900 | Readable dense text | Google Fonts |
| **Manrope** | 200–800 | Geometric, modern | Google Fonts |

### Editorial / Expressive (accent use, headings only)

| Font | Style | Best For |
|---|---|---|
| **Fraunces** | Optical-size serif | Dark editorial, luxury apps |
| **Instrument Serif** | Transitional serif | Editorial, writing tools |
| **Playfair Display** | High-contrast serif | Premium, publication-style |
| **Cabinet Grotesk** | Geometric sans | Modern brand, startups |
| **Satoshi** | Geometric sans | Tech-forward, clean |

### Monospace (code, data, terminal, logs)

| Font | Use Case |
|---|---|
| **JetBrains Mono** | Code editors, terminals, IDEs |
| **Geist Mono** | Companion to Geist UI font |
| **Fira Code** | Ligatures, developer tools |
| **Cascadia Code** | Windows-native feel |
| **Berkeley Mono** | Premium, editorial code |

---

## Forbidden Fonts

These fonts are overused in AI-generated UI. Avoid without explicit user request:

- `Inter` — statistical AI default
- `Roboto` — generic material default
- `Arial` — system fallback, never choose intentionally
- `Open Sans` — dated, overused
- `Lato` — dated corporate
- `Space Grotesk` — recent AI overuse

---

## Typographic Scale

Use mathematical ratios — never arbitrary sizes.

### Major Third (×1.25) — Dense UI / Tool
```css
--text-xs:   0.64rem;   /* 10.2px — captions, badges */
--text-sm:   0.8rem;    /* 12.8px — secondary labels */
--text-base: 1rem;      /* 16px   — body, default */
--text-md:   1.25rem;   /* 20px   — subheadings */
--text-lg:   1.563rem;  /* 25px   — section headings */
--text-xl:   1.953rem;  /* 31px   — page titles */
--text-2xl:  2.441rem;  /* 39px   — hero titles */
```

### Perfect Fourth (×1.333) — Editorial / Spacious
```css
--text-xs:   0.563rem;  /* 9px  */
--text-sm:   0.75rem;   /* 12px */
--text-base: 1rem;      /* 16px */
--text-md:   1.333rem;  /* 21px */
--text-lg:   1.777rem;  /* 28px */
--text-xl:   2.369rem;  /* 38px */
--text-2xl:  3.157rem;  /* 51px */
```

### Desktop-Specific Sizing Rules

- Sidebar labels: `--text-sm` (12–13px)
- Table cell text: `--text-sm` (12–13px)
- Form inputs: `--text-base` (14–16px)
- Tooltips: `--text-xs` (11–12px)
- Page headings: `--text-lg` or `--text-xl`
- Breadcrumbs: `--text-sm`

---

## Line Height

| Context | Line Height |
|---|---|
| UI labels, badges, buttons | `1.2` |
| Form inputs, table cells | `1.4` |
| Body paragraphs | `1.6–1.7` |
| Headings | `1.1–1.2` |
| Code blocks | `1.6` |

---

## Letter Spacing

| Context | Tracking |
|---|---|
| Uppercase labels | `0.05–0.08em` |
| Regular headings | `−0.01em` to `−0.02em` (tight) |
| Body text | `0` or `0.01em` |
| Monospace | `0` |

---

## Font Pairing Recipes for Desktop Apps

### Developer Tool / Terminal-adjacent
```
Headings: Geist (600–700)
Body: Geist (400)
Code: Geist Mono (400)
```

### SaaS Dashboard
```
Headings: Plus Jakarta Sans (700)
Body: DM Sans (400)
Data: IBM Plex Sans (400, tabular-nums)
```

### Editorial / Writing Tool (Notion-like)
```
Headings: Instrument Serif (400) or Fraunces (400)
Body: DM Sans (400)
Code: JetBrains Mono (400)
```

### Premium Dark App (Superhuman-like)
```
Headings: Cabinet Grotesk (700) or Satoshi (700)
Body: Outfit (400)
Code: Fira Code (400)
```

### Enterprise Data Tool
```
All text: IBM Plex Sans
Code/values: IBM Plex Mono
```

---

## Numeric Display Rules

Always on metric/data values:
```css
font-variant-numeric: tabular-nums;
font-feature-settings: 'tnum' 1;
```

---

## Heading Balance

Always on headings under ~4 words:
```css
text-wrap: balance;
```

---

## Text Color Rules

- Body text: never `#000` / `black` — use `#111111`, `#1C1C1E`, or `var(--text-primary)`
- Secondary text: `#6B7280` minimum on white (contrast 4.6:1 ✓)
- Disabled text: `#9CA3AF` on white (3:1, acceptable for disabled)
- Dark mode body: `#F5F5F5` or `#E8E8E8` — never pure `#FFFFFF` (too harsh)
- Dark mode secondary: `#9CA3AF` on `#1a1a1a` (contrast verified)
