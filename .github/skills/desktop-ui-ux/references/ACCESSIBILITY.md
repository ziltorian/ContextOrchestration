# Accessibility Reference — WCAG 2.2

## Priority Order for Desktop Apps

Desktop users include power users with keyboards, screen readers, and switch devices.
Keyboard accessibility is non-negotiable.

---

## Critical (Ship-Blockers)

### 1. Focus Visibility (WCAG 2.4.7 / 2.4.11)

Every interactive element must have a visible focus indicator.
Never do this: `*:focus { outline: none; }` or `button:focus { outline: 0; }` without a replacement.

```css
/* Minimum — 2px offset outline */
:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
}

/* Better — matches element shape */
.btn:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
  border-radius: inherit;
}

/* For dark backgrounds — white focus ring */
.dark :focus-visible {
  outline-color: rgba(255,255,255,0.7);
}
```

### 2. Keyboard Navigation

- All actions reachable by Tab, Shift+Tab
- Lists with keyboard selection: arrow keys (↑↓) navigate items, Enter/Space select
- Modals: trap focus inside while open; return focus to trigger on close
- Command palette: ↑↓ navigate, Enter execute, Esc close
- Sidebar collapse: keyboard-accessible toggle button
- Dropdowns: Esc closes, focus returns to trigger

Focus trap pattern (modal):
```javascript
function trapFocus(element) {
  const focusable = element.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const first = focusable[0];
  const last = focusable[focusable.length - 1];

  element.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;
    if (e.shiftKey) {
      if (document.activeElement === first) { e.preventDefault(); last.focus(); }
    } else {
      if (document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  first.focus();
}
```

### 3. Semantic HTML

Use the right element for the job:
- Navigation: `<nav>` with `aria-label`
- Main content: `<main>`
- Sidebar: `<aside>`
- Page header: `<header>`
- Page footer: `<footer>`
- Headings: `<h1>`–`<h6>` in hierarchy (no skipping)
- Buttons: `<button>` not `<div onclick=...>`
- Links: `<a href>` for navigation, `<button>` for actions
- Lists: `<ul>`/`<ol>` for item collections

### 4. Contrast Ratios

| Text Size | WCAG AA | WCAG AAA |
|---|---|---|
| Normal text (< 18pt) | 4.5:1 | 7:1 |
| Large text (≥ 18pt or 14pt bold) | 3:1 | 4.5:1 |
| UI components & graphics | 3:1 | — |

Minimum acceptable for desktop apps: **WCAG AA**.
Disabled elements are exempt from contrast requirements.

### 5. Form Accessibility

```html
<!-- ✅ Correct -->
<label for="name">Full name <span aria-hidden="true">*</span></label>
<input id="name" type="text" name="name" required aria-required="true"
       aria-describedby="name-error" />
<p id="name-error" role="alert" class="field-error" hidden>
  Name is required.
</p>

<!-- ❌ Wrong — placeholder only, no label -->
<input type="text" placeholder="Full name" />
```

Rules:
- Every input has a `<label>` with matching `for`/`id`
- Required fields: `required` attribute + `aria-required="true"` + visual indicator
- Errors: `role="alert"` + descriptive text (not just "Invalid")
- Error descriptions linked via `aria-describedby`

### 6. Icon-Only Buttons

```html
<!-- ✅ With aria-label -->
<button aria-label="Close dialog">
  <svg aria-hidden="true"><!-- × icon --></svg>
</button>

<!-- ✅ With visually hidden text -->
<button>
  <svg aria-hidden="true"><!-- × icon --></svg>
  <span class="sr-only">Close dialog</span>
</button>

<!-- ❌ No accessible name -->
<button><svg><!-- × icon --></svg></button>
```

```css
.sr-only {
  position: absolute;
  width: 1px; height: 1px;
  padding: 0; margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}
```

---

## Important (Fix Before Launch)

### 7. ARIA Patterns

Use ARIA only when semantic HTML is not enough:

| UI Component | Correct ARIA |
|---|---|
| Sidebar nav | `<nav aria-label="Main">`, items `aria-current="page"` |
| Command palette | `role="dialog"` `aria-modal="true"` `aria-label="..."` |
| Context menu | `role="menu"` items `role="menuitem"` |
| Data table sort | `aria-sort="ascending"` / `"descending"` / `"none"` |
| Tabs | `role="tablist"` `role="tab"` `aria-selected` `role="tabpanel"` |
| Sidebar toggle | `aria-expanded="true/false"` `aria-controls="sidebar-id"` |
| Resizable panel | `role="separator"` `aria-orientation` `aria-valuenow` `aria-valuemin` `aria-valuemax` |
| Live regions | `aria-live="polite"` for non-urgent; `aria-live="assertive"` for errors only |

### 8. Color Not Only Meaning (WCAG 1.4.1)

Never use color alone to convey meaning:
- Error state: red border + error icon + error message text
- Status badge: color + text label
- Sort direction: arrow icon + aria-sort attribute
- Selected/active: background change + aria-selected/aria-current

### 9. Heading Hierarchy

```html
<!-- ✅ Correct hierarchy -->
<h1>App Name</h1>
  <h2>Section Title</h2>
    <h3>Subsection</h3>

<!-- ❌ Skip — h1 then h3 -->
<h1>App Name</h1>
  <h3>Section Title</h3>  <!-- wrong: skipped h2 -->
```

### 10. Images

- Decorative icons: `aria-hidden="true"`
- Informative icons: `aria-label` on button or `alt` on `<img>`
- Complex charts: `aria-label` summary + accessible data table alternative

---

## Minimum Checklist Before Ship

```
□ All interactive elements reachable by Tab
□ Focus ring visible on all interactive elements
□ Focus trapped in open modals, returned on close
□ Arrow key navigation in lists/menus
□ All form inputs have associated <label>
□ Error messages: descriptive, linked with aria-describedby
□ Icon-only buttons have aria-label
□ Contrast ≥ 4.5:1 for text, 3:1 for UI components
□ Heading hierarchy without gaps
□ Semantic HTML: nav, main, aside, header used correctly
□ Color not sole means of conveying state
□ prefers-reduced-motion respected
□ prefers-color-scheme respected (if dark mode built)
□ Live regions for dynamic content updates
```
