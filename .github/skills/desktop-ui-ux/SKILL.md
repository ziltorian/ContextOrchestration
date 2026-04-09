---
name: desktop-ui-ux
description: >
  Expert UI/UX design for desktop applications (Electron, Tauri, native-shell) and
  localhost web apps (Vite, Next.js, Flask, FastAPI, Django dev server). Use this skill
  whenever the user asks to build, design, improve, or audit any interface for a desktop
  app or locally-hosted app — even if they don't say "UI" or "UX" explicitly.
  Triggers: "build a dashboard", "create a settings page", "design a sidebar",
  "make the UI look better", "add a toolbar", "implement dark mode", "build an admin panel",
  "create a data table", "make it look like VS Code / Linear / Notion",
  "improve the layout", "design components", "fix the navigation",
  "add keyboard shortcuts", "build a file tree", "create a command palette".
  Covers: aesthetic direction, typography, color systems, desktop-specific patterns
  (custom titlebars, resizable panels, sidebars, context menus, command palettes),
  keyboard navigation, accessibility (WCAG 2.2), motion, and anti-slop enforcement.
compatibility: VS Code with GitHub Copilot or similar AI coding assistants
metadata:
  version: "1.0"
  category: ui-ux-design
  author: ziltorian
---

# Desktop UI/UX Design

Build interfaces that feel crafted — not generated. For desktop apps and localhost web apps:
dense, keyboard-friendly, opinionated, with real design personality.

---

## Design Parameters (adapt to user request)

```
DESIGN_VARIANCE:  6   # 1=Perfect symmetry/minimal  10=Artsy/editorial chaos
MOTION_INTENSITY: 4   # 1=Static, no motion          10=Cinematic physics
VISUAL_DENSITY:   6   # 1=Art gallery / airy          10=Cockpit / packed data
```

Desktop apps skew toward higher density (5–8) than marketing sites (2–4).
Override these based on explicit user intent.

---

## Platform Context

Detect or ask about the runtime environment — it shapes what's possible:

| Platform | Key Constraints | UI Notes |
|---|---|---|
| **Electron** | Bundled Chromium, Node.js access | Can use any CSS/JS; custom window chrome feasible |
| **Tauri 2** | System WebView (WebKit/Blink/WebView2) | Avoid bleeding-edge CSS; native window controls |
| **Localhost web** | Browser tab, no native shell | Standard web constraints; no custom titlebar |
| **Flask/FastAPI/Django** | Server-rendered or SPA hybrid | Consider HTMX, minimal JS overhead |

---

## Workflow

### Step 1 — Assess Context (internal, do not show)

Identify:
- **Product type**: tool, dashboard, editor, viewer, settings, data explorer
- **Target users**: power users (keyboard-first) vs. casual (mouse-first)
- **Aesthetic direction**: see reference table below — commit to one
- **Platform**: Electron / Tauri / localhost browser tab
- **Stack**: React, Vue, Svelte, plain HTML+CSS, shadcn/ui, etc.
- **Data density**: sparse content vs. dense data tables/panels

### Step 2 — Choose Aesthetic Direction

Commit before writing code. Do not blend styles — pick one direction and hold it.

| Direction | Looks Like | Avoid Combining With |
|---|---|---|
| **Precision Dark** | Linear, Vercel Dashboard, Raycast | Colorful gradients, bounce animations |
| **Swiss Minimal** | Arc browser settings, Craft | Decorative borders, high density |
| **Editorial** | Notion, Bear, Obsidian | Neon accents, glassmorphism |
| **Neubrutalist** | Fig, Liveblocks | Soft shadows, rounded-everything |
| **OLED Luxury** | Superhuman, Reflect | Bright colors, high saturation |
| **Warm Neutral** | Things 3, Cron | Cold grays, harsh contrast |
| **Developer Dense** | VS Code, TablePlus, Postico | Hero sections, marketing copy |

Consult `references/TYPOGRAPHY.md` and `references/COLOR.md` for font/palette tables.

### Step 3 — Consult Reference Files

Load only what's needed:

- Typography choices → `references/TYPOGRAPHY.md`
- Color palette + tokens → `references/COLOR.md`
- Desktop-specific components → `references/COMPONENTS.md`
- Motion specs → `references/MOTION.md`
- Accessibility checklist → `references/ACCESSIBILITY.md`
- What to ban → `references/ANTI-PATTERNS.md`

### Step 4 — Generate Code

Implement with:
- CSS custom properties for every color and spacing token
- All interactive states: hover, focus, active, disabled, loading, error, empty
- Keyboard navigation where appropriate (Tab order, arrow keys in lists, Escape)
- Semantic HTML first, ARIA only when semantic HTML is insufficient
- Desktop viewport assumptions: min-width 1024px, no hamburger menus

### Step 5 — Self-Check Before Delivery

```
□ Aesthetic direction committed and consistent throughout
□ No forbidden fonts (Inter, Roboto, Arial, Open Sans, Space Grotesk)
□ No purple/blue AI gradient without explicit request
□ CSS custom properties used for all tokens
□ All interactive states implemented
□ Keyboard navigation functional
□ Focus rings visible (not removed)
□ Contrast ≥ 4.5:1 for text, ≥ 3:1 for UI components
□ Touch targets not applicable (desktop) — click targets ≥ 32px height
□ No placeholder-as-label in forms
□ Icon-only buttons have aria-label
□ Heading hierarchy without gaps (h1 → h2, not h1 → h3)
□ prefers-reduced-motion respected
□ prefers-color-scheme respected (if dark mode implemented)
□ No Unsplash links (use picsum.photos or SVG placeholders)
□ No AI-copywriting clichés ("Seamless", "Elevate", "Unleash", "Next-Gen")
```

---

## Desktop-Specific Design Rules

### Layout

- **No hamburger menus.** Desktop apps use persistent sidebars or top navigation bars.
- **Sidebar widths**: collapsed 48–56px (icons only), expanded 220–260px
- **Panel layouts**: use CSS Grid or `display: flex` with resizable splitter handles
- **Content max-width**: constrain text columns to `max-w-2xl`–`max-w-4xl`; data tables span full width
- **Density modes**: implement compact / comfortable / spacious variants for power users
- **Keyboard shortcut hints**: show `⌘K`, `Ctrl+P` etc. inline on hover or in command palette

### Navigation Patterns

Prefer for desktop apps:
1. **Vertical sidebar** with icons + labels (expanded) or icons-only (collapsed)
2. **Tab bar** for document-style apps (editors, browsers)
3. **Top nav + sub-nav** for tool-style apps with deep sections

Avoid:
- Hamburger menus on desktop
- Bottom navigation (mobile pattern)
- Full-page overlays for primary navigation

### Window Chrome (Electron / Tauri only)

When implementing custom window controls:
- Use `-webkit-app-region: drag` on the titlebar area
- Place window controls (close/minimize/maximize) in OS-native position:
  - macOS: top-left traffic lights
  - Windows: top-right ×□—
- Title text: centered on macOS, left-aligned on Windows
- Titlebar height: 36–40px; total draggable area must be ≥ 36px tall

### Command Palette

Every power-user app benefits from one. Implement with:
- Trigger: `⌘K` / `Ctrl+K`
- Full-screen overlay with centered modal, blurred backdrop
- Fuzzy search input, instant filtering
- Keyboard navigation: ↑↓ to select, Enter to execute, Esc to close
- Show keyboard shortcut next to each action

### Context Menus

- Trigger: right-click on interactive elements
- Width: 160–240px; item height: 28–32px
- Include icons (16px) before labels
- Separator lines between logical groups
- Danger actions (delete, remove): red text, bottom of menu

### Data Tables

For data-heavy UIs:
- Header: sticky top, clear sort indicators (↑↓ arrows)
- Row height: compact 32px, comfortable 40px, spacious 48px
- Alternating row bg: subtle, not high-contrast zebra
- Column resize handles: visible on hover
- Keyboard: arrow keys navigate cells, Enter/Space activate
- Selection state: clear highlight + checkbox

---

## Typography Rules

Full reference in `references/TYPOGRAPHY.md`. Quick rules:

**Forbidden fonts (without explicit user request):**
`Inter`, `Roboto`, `Arial`, `Open Sans`, `Lato`, `Space Grotesk` (AI overuse)

**Preferred for desktop apps:**
- UI / System: `Geist`, `Outfit`, `DM Sans`, `Plus Jakarta Sans`
- Editorial accent: `Fraunces`, `Instrument Serif`, `Playfair Display`
- Monospace: `JetBrains Mono`, `Geist Mono`, `Fira Code`
- Dense data: `IBM Plex Sans`, `Source Sans 3`

**Non-negotiable:**
- Body text never `#000000` — use `#111111`, `#1a1a1a`, or CSS token
- Secondary text: minimum gray-500 on white, gray-400 on dark bg (check contrast)
- `font-variant-numeric: tabular-nums` on all data/metric displays
- `text-wrap: balance` on headings
- Form inputs: minimum 14px (desktop can go lower than 16px mobile rule)

---

## Color Rules

Full reference in `references/COLOR.md`. Quick rules:

- All colors via CSS custom properties — never hardcoded hex in components
- Maximum 1 primary accent color + neutral scale
- Saturation < 75% for accent colors (prevents "AI purple" aesthetic)
- Dark mode: use `prefers-color-scheme` + `.dark` class hybrid approach
- **The LILA Ban**: no purple/blue glow, no `#7C3AED`/`#6366f1` default purple

---

## Motion Rules

Full reference in `references/MOTION.md`. Quick rules:

- Sidebar expand/collapse: `200ms ease-out`
- Modal open: `150ms ease-out` (scale 0.95→1 + opacity 0→1)
- Tooltip: `100ms ease-out` delay 400ms
- Page transition: `200ms ease-in-out`
- **Never**: bounce/elastic easing for UI elements
- **Always**: `@media (prefers-reduced-motion: reduce)` — set `transition: none`
- CSS-only for hover/focus transitions; Framer Motion for complex sequences
- Do not mix Framer Motion and GSAP in the same component tree

---

## Accessibility

Full checklist in `references/ACCESSIBILITY.md`. Desktop minimum:

- All functionality reachable via keyboard
- Visible focus ring on every interactive element (never `outline: none` without replacement)
- Screen reader: semantic landmarks (`main`, `nav`, `aside`, `header`)
- ARIA roles only when semantic HTML is insufficient
- Contrast: 4.5:1 text, 3:1 large text and UI components
- Error messages: describe what happened + how to fix, not just "Error"

---

## Anti-Patterns

See `references/ANTI-PATTERNS.md` for full list. Hard bans:

**Visual:**
- Purple-cyan gradients (AI aesthetic)
- Gradient text on metrics/numbers
- Glassmorphism without explicit request
- Glow effects (box-shadow with spread + color)
- Identical 3-column card grids as default layout
- ALL CAPS for primary content

**Interaction:**
- Bounce/elastic easing on UI elements
- Removing focus outlines without replacement
- Placeholder text as the only label for form inputs

**Code:**
- Boolean prop proliferation (`isCompact`, `showHeader`, `isRounded` all in one component)
- Barrel imports from large libraries (import directly)
- Color-only meaning without icon/text fallback

**Copy:**
- "Acme", "Nexus", "SmartFlow" as placeholder brand names
- "Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionize"
- Unsplash URLs (use `https://picsum.photos/seed/{word}/800/600`)
