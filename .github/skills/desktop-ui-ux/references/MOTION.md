# Motion Reference

## Core Principle

One well-orchestrated interaction > scattered micro-animations.
Desktop apps have power users — motion must be purposeful, not decorative.

---

## Duration Table

| Interaction | Duration | Why |
|---|---|---|
| Hover state (bg, color) | 80–120ms | Feels immediate |
| Button press feedback | 80ms | Tactile, instant |
| Tooltip appear | 100ms + 400ms delay | Fast once triggered |
| Sidebar item highlight | 100ms | Fluid tracking |
| Dropdown/popover open | 120–150ms | Snappy |
| Modal open | 150ms | Present without lag |
| Modal close | 100ms | Faster exit feels clean |
| Sidebar expand/collapse | 200ms | Layout change, needs weight |
| Panel resize | 0ms (real-time drag) | Never animate drag |
| Page / route transition | 180–220ms | Smooth navigation |
| Toast appear | 200ms | Noticeable entrance |
| Toast disappear | 150ms | Quick exit |
| Command palette open | 120ms | Must feel instant |
| Skeleton → content | 200ms | Fade, not pop |

**Rule**: Never exceed 300ms for UI transitions. If you think it needs 400ms+, reconsider whether animation is appropriate at all.

---

## Easing Reference

```css
/* Core easings as CSS custom properties */
:root {
  --ease-standard:   cubic-bezier(0.4, 0, 0.2, 1);  /* material standard */
  --ease-decelerate: cubic-bezier(0, 0, 0.2, 1);    /* entering elements */
  --ease-accelerate: cubic-bezier(0.4, 0, 1, 1);    /* exiting elements */
  --ease-sharp:      cubic-bezier(0.4, 0, 0.6, 1);  /* quick transitions */
  --ease-out:        cubic-bezier(0, 0, 0.3, 1);    /* general exit */
  --ease-in-out:     cubic-bezier(0.4, 0, 0.2, 1);
}
```

### When to Use Each

| Easing | Use For | Never Use For |
|---|---|---|
| `ease-out` | Elements entering screen | Loops, exits |
| `ease-in` | Elements leaving screen | Entrances |
| `ease-standard` | Position changes, layout | New elements appearing |
| `ease-decelerate` | Modals, drawers opening | Subtle hover states |
| `ease-accelerate` | Modals, drawers closing | Entrances |

### Forbidden Easings

- `ease` (CSS default) — imprecise, inconsistent feel
- `bounce` / `elastic` — toy physics, not UI
- `linear` on opacity/color — looks mechanical
- Spring physics on UI chrome (OK for creative apps only)

---

## Pattern Recipes

### Sidebar Collapse

```css
.sidebar {
  width: var(--sidebar-width);
  transition: width var(--sidebar-duration, 200ms) var(--ease-standard);
  overflow: hidden;
}
.sidebar.collapsed { width: 56px; }
```

### Modal Open / Close

```css
/* Using View Transitions API (modern browsers) */
@starting-style {
  .modal { opacity: 0; transform: scale(0.96) translateY(4px); }
}
.modal {
  opacity: 1; transform: scale(1) translateY(0);
  transition: opacity 150ms var(--ease-decelerate),
              transform 150ms var(--ease-decelerate);
}
.modal.closing {
  opacity: 0; transform: scale(0.96) translateY(4px);
  transition-duration: 100ms;
  transition-timing-function: var(--ease-accelerate);
}

/* Backdrop */
.backdrop {
  opacity: 1;
  transition: opacity 150ms var(--ease-standard);
}
.backdrop.closing { opacity: 0; transition-duration: 100ms; }
```

### Command Palette Open

```css
.cmd-backdrop {
  animation: cmd-backdrop-in 120ms var(--ease-decelerate) forwards;
}
.cmd-modal {
  animation: cmd-modal-in 120ms var(--ease-decelerate) forwards;
}
@keyframes cmd-backdrop-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}
@keyframes cmd-modal-in {
  from { opacity: 0; transform: scale(0.97) translateY(-8px); }
  to   { opacity: 1; transform: scale(1) translateY(0); }
}
```

### Toast Entrance

```css
.toast {
  animation: toast-in 200ms var(--ease-decelerate) forwards;
}
@keyframes toast-in {
  from { opacity: 0; transform: translateX(16px); }
  to   { opacity: 1; transform: translateX(0); }
}
```

### Skeleton Loading

```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--bg-sunken) 25%,
    var(--border-subtle) 50%,
    var(--bg-sunken) 75%
  );
  background-size: 200% 100%;
  animation: skeleton-sweep 1.4s ease-in-out infinite;
}
@keyframes skeleton-sweep {
  from { background-position: 200% 0; }
  to   { background-position: -200% 0; }
}
```

### Page / Route Transition

```css
/* With View Transitions API */
@view-transition { navigation: auto; }

/* Manual */
.page {
  animation: page-in 200ms var(--ease-decelerate) forwards;
}
@keyframes page-in {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

---

## Reduced Motion

**Always implement this.** Do not skip it.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

For Framer Motion (React):
```jsx
import { useReducedMotion } from 'framer-motion';
const prefersReduced = useReducedMotion();

<motion.div
  animate={{ opacity: 1 }}
  transition={{ duration: prefersReduced ? 0 : 0.15 }}
/>
```

---

## Library Selection

| Need | Library | Avoid With |
|---|---|---|
| Simple hover/focus transitions | CSS only | — |
| Component enter/exit | Framer Motion | GSAP in same tree |
| Complex sequences, stagger | Framer Motion `AnimatePresence` | GSAP in same tree |
| Scroll-driven narrative sections | GSAP ScrollTrigger | Framer Motion in same tree |
| Canvas / WebGL | Three.js, GSAP | Framer Motion |
| Page transitions (Next.js) | Framer Motion layout animations | — |

**Hard rule**: Do not mix Framer Motion and GSAP in the same React component tree.
They use different animation loops and will conflict in practice.
