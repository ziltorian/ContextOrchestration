# Anti-Patterns — Explicit Bans

These patterns mark output as AI-generated or low-quality.
This file defines hard NO rules. When you catch yourself about to use these, stop.

---

## Visual Anti-Patterns

### The AI Purple Aesthetic
```
❌ background: linear-gradient(135deg, #7C3AED, #06B6D4)
❌ color: #8B5CF6 as primary action color
❌ box-shadow: 0 0 20px rgba(139, 92, 246, 0.5)   ← glow
❌ background: linear-gradient(to right, #6366f1, #8b5cf6)

✅ Pick a non-purple accent from COLOR.md
✅ Use single hue, no gradient on chrome elements
```

### Gradient Text on Numbers
```
❌ .metric-value {
    background: linear-gradient(135deg, #6366f1, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
   }

✅ .metric-value { color: var(--text-primary); font-variant-numeric: tabular-nums; }
```

### Glassmorphism on Everything
Only acceptable when explicitly requested or for floating overlays on image backgrounds.
```
❌ Using backdrop-filter: blur() on sidebars, cards, panels
❌ background: rgba(255,255,255,0.1) on solid-color backgrounds

✅ Solid background with proper border and shadow
✅ Glass effect only on modals/toasts over imagery (when needed)
```

### Glow Effects
```
❌ box-shadow: 0 0 15px rgba(99, 102, 241, 0.4)
❌ box-shadow: 0 0 30px rgba(0, 0, 0, 0.5), 0 0 60px rgba(139, 92, 246, 0.3)

✅ box-shadow: var(--shadow-md)   ← directional, not radial
```

### Identical 3-Column Card Grid
```
❌ <div class="grid grid-cols-3 gap-6">
     <Card /> <Card /> <Card />
   </div>
   (with cards having same aspect ratio, same padding, same border-radius)

✅ Vary density: one wide feature card + two narrow cards
✅ Use bento-style layout with different cell sizes
✅ Use list view if data is tabular
```

### ALL CAPS for Primary Content
```
❌ <h2 class="uppercase">DASHBOARD OVERVIEW</h2>
❌ .section-label { text-transform: uppercase; font-size: 14px; }

✅ ALL CAPS acceptable ONLY for: keyboard shortcuts (⌘K), badge labels under 6 chars, chart axis labels
✅ Use font-weight variation instead of case for emphasis
```

### Decorative Borders and Dividers
```
❌ border: 2px dashed var(--border-default)   ← decorative dashes
❌ border-left: 4px solid var(--accent-500)   ← colored accent border on cards without semantic purpose
❌ Excessive horizontal rules between every section

✅ Use negative space (padding/margin) to separate sections
✅ Use subtle 1px border only where needed for structural clarity
```

### Hero Metric Layout
```
❌ Three cards with giant centered numbers, gradient text, decorative icons, percentage pills

✅ Data table for comparable metrics
✅ Sparkline chart for trends
✅ If using cards: add context (label, change indicator, time period)
```

---

## Interaction Anti-Patterns

### Bounce / Elastic Easing
```
❌ transition: transform 400ms cubic-bezier(0.175, 0.885, 0.32, 1.275)
❌ spring: { type: "spring", bounce: 0.4, duration: 0.6 }
❌ animation: popup 300ms bounce

✅ transition: transform 150ms cubic-bezier(0, 0, 0.2, 1)
```

### Removing Focus Outlines
```
❌ * { outline: none; }
❌ button:focus { outline: 0; }
❌ :focus { outline: none; }

✅ :focus-visible { outline: 2px solid var(--border-focus); outline-offset: 2px; }
```

### Placeholder as Label
```
❌ <input type="email" placeholder="Email address" />  ← no label element

✅ <label for="email">Email address</label>
   <input id="email" type="email" placeholder="you@example.com" />
```

### Mobile Patterns on Desktop
```
❌ Hamburger menu that opens a full-screen overlay navigation
❌ Bottom navigation bar (48px bar at screen bottom)
❌ Full-screen modals for confirmations
❌ Swipe-to-delete as only delete mechanism

✅ Persistent sidebar navigation
✅ Compact dropdown menus
✅ Context menus for item actions
✅ Keyboard-accessible confirmation dialogs
```

---

## Code Anti-Patterns

### Boolean Prop Proliferation
```
❌ <Button
     isCompact
     showIcon
     isRounded
     hasBorder
     isLoading
     isDanger
   />

✅ <Button variant="ghost" size="sm" />
✅ <Button.Danger loading />
```

### Barrel Imports from Large Libraries
```
❌ import { Button, Input, Modal, Toast, Badge } from '@/components/ui'

✅ import { Button } from '@/components/ui/button'
✅ import { Input } from '@/components/ui/input'
```

### Color-Only Meaning
```
❌ <span style="color: red">3 errors</span>  ← color only

✅ <span>
     <svg aria-hidden="true" class="icon-error"><!-- ! icon --></svg>
     <span style="color: var(--status-error)">3 errors</span>
   </span>
```

---

## Copy Anti-Patterns

### AI Startup Clichés
```
❌ Product names: "Nexus", "Acme", "SmartFlow", "Synapse", "Pulse"
❌ Taglines: "Elevate your workflow", "Seamless collaboration",
             "Unleash your potential", "Next-Gen productivity",
             "Revolutionize the way you work"
❌ CTAs: "Get Started Today!", "Transform Your Business"

✅ Descriptive names: "Inbox", "Tasks", "Settings", "Reports"
✅ Specific CTAs: "Create project", "Add team member", "Export CSV"
```

### Broken Image Sources
```
❌ https://source.unsplash.com/random   ← frequently broken
❌ https://picsum.photos/200/200        ← OK but generic

✅ https://picsum.photos/seed/keyword/800/400   ← deterministic seed
✅ SVG placeholder with initials/icon
✅ CSS gradient placeholder as background
```

---

## Desktop-Specific Anti-Patterns

### Ignoring Keyboard Shortcuts
```
❌ Building a developer tool with zero keyboard shortcuts
❌ No ⌘K / Ctrl+K command palette in a tool app

✅ Show keyboard hints in sidebar items on hover
✅ Implement ⌘K command palette for all apps
✅ Esc closes any focused overlay
```

### Too Much Padding for Data-Dense Views
```
❌ 24px padding on every table cell in a data-heavy screen
❌ 32px gap between sidebar items in a dense developer tool

✅ 8px padding on table cells (compact mode)
✅ 6px padding / 32px height for sidebar items
```

### Window Chrome Mistakes (Electron/Tauri)
```
❌ No custom titlebar → looks like a browser tab
❌ Custom titlebar without -webkit-app-region: drag
❌ Placing the macOS window controls on the right side
❌ Titlebar < 36px tall (insufficient drag area)

✅ Set -webkit-app-region: drag on titlebar area
✅ -webkit-app-region: no-drag on interactive elements inside titlebar
✅ macOS: traffic lights on left; Windows: controls on right
```
