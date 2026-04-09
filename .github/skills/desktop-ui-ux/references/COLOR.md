# Color Reference

## Core Principle

All colors via CSS custom properties. Never hardcode hex values in components.
One accent color maximum. Neutral scale is the foundation.

---

## Forbidden Color Patterns ("The AI Aesthetic")

These patterns mark AI-generated output. Avoid without explicit request:

- `#7C3AED` / `#6366f1` — AI purple defaults
- Purple-to-blue gradients on any background
- Cyan-to-purple gradient (`#06B6D4` → `#8B5CF6`)
- Neon green / electric blue accents on dark backgrounds
- Gradient text on numbers, metrics, or KPIs
- Aurora/mesh gradient backgrounds
- Glow effects (`box-shadow: 0 0 20px rgba(139, 92, 246, 0.5)`)

---

## Recommended Neutral Bases

Choose one. Neutrals are 90% of your UI.

### Zinc (cold, modern — Linear, Vercel)
```css
--neutral-50:  #fafafa;
--neutral-100: #f4f4f5;
--neutral-200: #e4e4e7;
--neutral-300: #d4d4d8;
--neutral-400: #a1a1aa;
--neutral-500: #71717a;
--neutral-600: #52525b;
--neutral-700: #3f3f46;
--neutral-800: #27272a;
--neutral-900: #18181b;
--neutral-950: #09090b;
```

### Slate (slightly blue-cool — Tailwind default, clean)
```css
--neutral-50:  #f8fafc;
--neutral-100: #f1f5f9;
--neutral-200: #e2e8f0;
--neutral-300: #cbd5e1;
--neutral-400: #94a3b8;
--neutral-500: #64748b;
--neutral-600: #475569;
--neutral-700: #334155;
--neutral-800: #1e293b;
--neutral-900: #0f172a;
--neutral-950: #020617;
```

### Stone (warm neutral — Notion, writing tools)
```css
--neutral-50:  #fafaf9;
--neutral-100: #f5f5f4;
--neutral-200: #e7e5e4;
--neutral-300: #d6d3d1;
--neutral-400: #a8a29e;
--neutral-500: #78716c;
--neutral-600: #57534e;
--neutral-700: #44403c;
--neutral-800: #292524;
--neutral-900: #1c1917;
--neutral-950: #0c0a09;
```

---

## Accent Color Palettes

Pick one. Saturation must be < 75% for readable UI accents.

### Electric Blue (developer tools, technical)
```css
--accent-50:  #eff6ff;
--accent-100: #dbeafe;
--accent-400: #60a5fa;
--accent-500: #3b82f6;
--accent-600: #2563eb;   /* primary action */
--accent-700: #1d4ed8;   /* hover */
--accent-900: #1e3a8a;
```

### Teal (data tools, productivity)
```css
--accent-400: #2dd4bf;
--accent-500: #14b8a6;
--accent-600: #0d9488;   /* primary action */
--accent-700: #0f766e;   /* hover */
```

### Amber (warm, creative tools)
```css
--accent-400: #fbbf24;
--accent-500: #f59e0b;
--accent-600: #d97706;   /* primary action */
--accent-700: #b45309;   /* hover */
```

### Forest (calm, writing / notes)
```css
--accent-400: #4ade80;
--accent-500: #22c55e;
--accent-600: #16a34a;   /* primary action */
--accent-700: #15803d;   /* hover */
```

### Crimson (bold, brand-forward)
```css
--accent-500: #ef4444;
--accent-600: #dc2626;   /* primary action */
--accent-700: #b91c1c;   /* hover */
```

---

## Semantic Color System Template

```css
:root {
  /* Backgrounds */
  --bg-app:        var(--neutral-50);   /* outermost app shell */
  --bg-panel:      #ffffff;             /* sidebar, panels */
  --bg-elevated:   #ffffff;             /* cards, modals */
  --bg-sunken:     var(--neutral-100);  /* inputs, code blocks */
  --bg-overlay:    rgba(0,0,0,0.4);     /* modal backdrops */

  /* Text */
  --text-primary:   var(--neutral-900);
  --text-secondary: var(--neutral-500);
  --text-tertiary:  var(--neutral-400);
  --text-disabled:  var(--neutral-300);
  --text-inverse:   #ffffff;

  /* Borders */
  --border-subtle:  var(--neutral-100);
  --border-default: var(--neutral-200);
  --border-strong:  var(--neutral-300);
  --border-focus:   var(--accent-600);

  /* Interactive */
  --action-primary:       var(--accent-600);
  --action-primary-hover: var(--accent-700);
  --action-primary-text:  #ffffff;
  --action-secondary:     var(--neutral-100);
  --action-secondary-hover: var(--neutral-200);

  /* Status */
  --status-success:  #16a34a;
  --status-warning:  #d97706;
  --status-error:    #dc2626;
  --status-info:     #2563eb;

  /* Surfaces */
  --surface-hover:    rgba(0,0,0,0.04);
  --surface-selected: rgba(var(--accent-rgb), 0.08);
  --surface-active:   rgba(var(--accent-rgb), 0.12);

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -2px rgba(0,0,0,0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -4px rgba(0,0,0,0.04);
  --shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.05);
}
```

---

## Dark Mode Template

```css
.dark, [data-theme="dark"] {
  --bg-app:        var(--neutral-950);
  --bg-panel:      var(--neutral-900);
  --bg-elevated:   var(--neutral-800);
  --bg-sunken:     rgba(0,0,0,0.3);
  --bg-overlay:    rgba(0,0,0,0.6);

  --text-primary:   var(--neutral-50);
  --text-secondary: var(--neutral-400);
  --text-tertiary:  var(--neutral-500);
  --text-disabled:  var(--neutral-700);

  --border-subtle:  rgba(255,255,255,0.04);
  --border-default: rgba(255,255,255,0.08);
  --border-strong:  rgba(255,255,255,0.14);

  --surface-hover:    rgba(255,255,255,0.05);
  --surface-selected: rgba(var(--accent-rgb), 0.15);
  --surface-active:   rgba(var(--accent-rgb), 0.2);

  --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 8px rgba(0,0,0,0.4);
  --shadow-lg: 0 10px 20px rgba(0,0,0,0.5);
}
```

---

## WCAG Contrast Reference

| Pair | Ratio | WCAG AA | WCAG AAA |
|---|---|---|---|
| `#111111` on `#ffffff` | 19.6:1 | ✅ | ✅ |
| `#52525b` on `#ffffff` | 7.2:1  | ✅ | ✅ |
| `#71717a` on `#ffffff` | 4.6:1  | ✅ body | ✗ |
| `#a1a1aa` on `#ffffff` | 2.6:1  | ✗ | ✗ (disabled only) |
| `#ffffff` on `#2563eb` | 4.5:1  | ✅ | ✗ |
| `#ffffff` on `#09090b` | 19.6:1 | ✅ | ✅ |
| `#e4e4e7` on `#18181b` | 8.1:1  | ✅ | ✅ |
| `#71717a` on `#18181b` | 4.2:1  | ✗ | ✗ — use `#a1a1aa` instead |

**Requirement**: Text ≥ 4.5:1. Large text (18pt+ or 14pt bold) ≥ 3:1. UI components ≥ 3:1.

---

## Sidebar / Panel Color Recipe

```css
/* Light mode sidebar */
.sidebar {
  background: var(--bg-panel);       /* white or very light neutral */
  border-right: 1px solid var(--border-subtle);
}
.sidebar-item:hover  { background: var(--surface-hover); }
.sidebar-item.active { background: var(--surface-selected); color: var(--action-primary); }

/* Dark mode sidebar — slightly lighter than app bg */
.dark .sidebar {
  background: var(--neutral-900);     /* one step lighter than --bg-app */
  border-right: 1px solid var(--border-subtle);
}
```

---

## Data Visualization Colors

For charts, graphs, status indicators. Accessible palette (distinct at 3:1+ each):

```css
--data-blue:   #3b82f6;
--data-green:  #22c55e;
--data-amber:  #f59e0b;
--data-red:    #ef4444;
--data-violet: #8b5cf6;  /* OK in data viz, not UI chrome */
--data-teal:   #14b8a6;
--data-orange: #f97316;
```

Test all data colors against both light and dark backgrounds.
