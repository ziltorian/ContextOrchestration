# Desktop Component Patterns

## Sidebar Navigation

### Structure

```html
<nav class="sidebar" aria-label="Main navigation">
  <div class="sidebar-header">
    <!-- Logo / app name -->
  </div>
  <ul class="sidebar-nav" role="list">
    <li>
      <a href="/dashboard" class="sidebar-item" aria-current="page">
        <svg class="sidebar-icon" aria-hidden="true">...</svg>
        <span class="sidebar-label">Dashboard</span>
        <kbd class="sidebar-shortcut">⌘1</kbd>
      </a>
    </li>
  </ul>
  <div class="sidebar-footer">
    <!-- User profile, settings -->
  </div>
</nav>
```

### CSS

```css
.sidebar {
  width: var(--sidebar-width, 240px);
  min-width: 240px;
  height: 100vh;
  background: var(--bg-panel);
  border-right: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: width 200ms ease-out;
}
.sidebar.collapsed { width: 56px; }
.sidebar.collapsed .sidebar-label,
.sidebar.collapsed .sidebar-shortcut { display: none; }

.sidebar-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px;
  height: 32px;
  border-radius: 6px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 13px;
  font-weight: 450;
  cursor: pointer;
  transition: background 120ms ease, color 120ms ease;
}
.sidebar-item:hover  { background: var(--surface-hover); color: var(--text-primary); }
.sidebar-item:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: -1px;
}
.sidebar-item[aria-current="page"] {
  background: var(--surface-selected);
  color: var(--action-primary);
  font-weight: 500;
}
.sidebar-icon { width: 16px; height: 16px; flex-shrink: 0; }
.sidebar-shortcut {
  margin-left: auto;
  font-size: 11px;
  color: var(--text-tertiary);
  background: var(--bg-sunken);
  padding: 1px 4px;
  border-radius: 3px;
  font-family: var(--font-mono);
}
```

---

## Resizable Panel Layout

```html
<div class="panel-layout">
  <aside class="panel panel-left" style="width: 260px">...</aside>
  <div class="panel-resizer" role="separator" aria-orientation="vertical"
       aria-valuenow="260" aria-valuemin="180" aria-valuemax="500"
       tabindex="0"></div>
  <main class="panel panel-main">...</main>
</div>
```

```css
.panel-layout {
  display: flex;
  height: 100vh;
  overflow: hidden;
}
.panel-resizer {
  width: 4px;
  cursor: col-resize;
  background: transparent;
  flex-shrink: 0;
  transition: background 150ms;
}
.panel-resizer:hover,
.panel-resizer:focus-visible { background: var(--border-focus); }
.panel-resizer:focus-visible { outline: none; }
```

---

## Command Palette

```html
<div class="cmd-backdrop" role="dialog" aria-modal="true" aria-label="Command palette">
  <div class="cmd-modal">
    <div class="cmd-search">
      <svg class="cmd-search-icon" aria-hidden="true"><!-- search icon --></svg>
      <input
        type="text"
        class="cmd-input"
        placeholder="Type a command or search..."
        aria-autocomplete="list"
        aria-controls="cmd-results"
        autocomplete="off"
        spellcheck="false"
      />
      <kbd class="cmd-esc-hint">Esc</kbd>
    </div>
    <ul id="cmd-results" class="cmd-list" role="listbox">
      <li class="cmd-group-label">Recent</li>
      <li class="cmd-item" role="option" aria-selected="true">
        <svg class="cmd-item-icon" aria-hidden="true">...</svg>
        <span class="cmd-item-label">Open Settings</span>
        <kbd class="cmd-item-shortcut">⌘,</kbd>
      </li>
    </ul>
    <div class="cmd-footer">
      <span><kbd>↑↓</kbd> navigate</span>
      <span><kbd>↵</kbd> select</span>
      <span><kbd>Esc</kbd> close</span>
    </div>
  </div>
</div>
```

```css
.cmd-backdrop {
  position: fixed; inset: 0;
  background: var(--bg-overlay);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 15vh;
  z-index: 1000;
}
.cmd-modal {
  width: 560px;
  max-height: 60vh;
  background: var(--bg-elevated);
  border: 1px solid var(--border-default);
  border-radius: 12px;
  box-shadow: var(--shadow-xl);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.cmd-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: 15px;
  color: var(--text-primary);
  padding: 0;
}
.cmd-search {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  border-bottom: 1px solid var(--border-subtle);
}
.cmd-list {
  flex: 1;
  overflow-y: auto;
  padding: 6px;
  list-style: none;
  margin: 0;
}
.cmd-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 7px 10px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  color: var(--text-primary);
}
.cmd-item[aria-selected="true"] { background: var(--surface-selected); }
.cmd-item:hover { background: var(--surface-hover); }
.cmd-item-shortcut { margin-left: auto; color: var(--text-tertiary); }
.cmd-footer {
  display: flex;
  gap: 12px;
  padding: 8px 14px;
  font-size: 11px;
  color: var(--text-tertiary);
  border-top: 1px solid var(--border-subtle);
}
```

---

## Context Menu

```html
<ul class="context-menu" role="menu" style="position: fixed; top: X; left: Y">
  <li role="menuitem" class="context-item">
    <svg aria-hidden="true">...</svg>
    Open in New Tab
    <kbd>⌘↵</kbd>
  </li>
  <li class="context-separator" role="separator"></li>
  <li role="menuitem" class="context-item context-item--danger">
    <svg aria-hidden="true">...</svg>
    Delete
    <kbd>⌫</kbd>
  </li>
</ul>
```

```css
.context-menu {
  min-width: 180px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-default);
  border-radius: 8px;
  box-shadow: var(--shadow-lg);
  padding: 4px;
  list-style: none;
  margin: 0;
  z-index: 900;
}
.context-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 5px 8px;
  border-radius: 5px;
  font-size: 13px;
  color: var(--text-primary);
  cursor: pointer;
}
.context-item:hover { background: var(--surface-hover); }
.context-item:focus-visible {
  outline: none;
  background: var(--surface-hover);
}
.context-item kbd { margin-left: auto; color: var(--text-tertiary); font-size: 11px; }
.context-item--danger { color: var(--status-error); }
.context-item--danger:hover { background: rgba(220, 38, 38, 0.08); }
.context-separator {
  height: 1px;
  background: var(--border-subtle);
  margin: 3px 0;
}
```

---

## Data Table

```html
<div class="table-wrapper">
  <table class="data-table" aria-label="Users">
    <thead>
      <tr>
        <th scope="col" class="th-sortable" aria-sort="ascending">
          Name
          <svg class="sort-icon" aria-hidden="true"><!-- up arrow --></svg>
        </th>
        <th scope="col">Email</th>
        <th scope="col" class="th-numeric">Created</th>
        <th scope="col" class="th-actions"><span class="sr-only">Actions</span></th>
      </tr>
    </thead>
    <tbody>
      <tr class="tr-row">
        <td class="td-primary">Alice Johnson</td>
        <td class="td-secondary">alice@example.com</td>
        <td class="td-numeric">2024-03-15</td>
        <td class="td-actions">
          <button aria-label="Edit Alice Johnson" class="btn-ghost-sm">Edit</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

```css
.table-wrapper { overflow-x: auto; }
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}
.data-table thead th {
  position: sticky; top: 0;
  background: var(--bg-panel);
  border-bottom: 1px solid var(--border-default);
  padding: 8px 12px;
  font-weight: 500;
  color: var(--text-secondary);
  text-align: left;
  white-space: nowrap;
  z-index: 1;
}
.th-sortable { cursor: pointer; user-select: none; }
.th-sortable:hover { color: var(--text-primary); }
.th-numeric { text-align: right; }
.data-table tbody tr {
  border-bottom: 1px solid var(--border-subtle);
  transition: background 80ms;
}
.data-table tbody tr:hover { background: var(--surface-hover); }
.data-table td { padding: 8px 12px; color: var(--text-primary); }
.td-secondary { color: var(--text-secondary); }
.td-numeric {
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}
.td-actions { text-align: right; width: 1%; white-space: nowrap; }
```

---

## Custom Titlebar (Electron / Tauri)

```html
<div class="titlebar" data-tauri-drag-region>
  <!-- macOS: leave space for traffic lights (72px left padding) -->
  <div class="titlebar-controls-left" aria-hidden="true">
    <!-- Electron: custom buttons or native -->
  </div>
  <span class="titlebar-title">App Name — Document</span>
  <div class="titlebar-controls-right">
    <button class="titlebar-btn" aria-label="Minimize">—</button>
    <button class="titlebar-btn" aria-label="Maximize">□</button>
    <button class="titlebar-btn titlebar-btn--close" aria-label="Close">✕</button>
  </div>
</div>
```

```css
.titlebar {
  height: 38px;
  background: var(--bg-panel);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  -webkit-app-region: drag;          /* Electron / Tauri drag region */
  user-select: none;
  flex-shrink: 0;
}
.titlebar-title {
  font-size: 13px;
  font-weight: 500;
  color: var(--text-secondary);
}
.titlebar-btn {
  -webkit-app-region: no-drag;       /* must opt out of drag for buttons */
  /* style as needed */
}
```

---

## Toast / Notification

```html
<div role="status" aria-live="polite" aria-atomic="true" class="toast toast--success">
  <svg class="toast-icon" aria-hidden="true"><!-- check icon --></svg>
  <div class="toast-body">
    <p class="toast-title">Changes saved</p>
    <p class="toast-desc">Your document was saved successfully.</p>
  </div>
  <button class="toast-dismiss" aria-label="Dismiss notification">✕</button>
</div>
```

```css
.toast {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 12px 14px;
  background: var(--bg-elevated);
  border: 1px solid var(--border-default);
  border-radius: 8px;
  box-shadow: var(--shadow-lg);
  min-width: 280px;
  max-width: 380px;
  font-size: 13px;
}
.toast--success { border-left: 3px solid var(--status-success); }
.toast--error   { border-left: 3px solid var(--status-error); }
.toast--warning { border-left: 3px solid var(--status-warning); }
.toast-title { font-weight: 500; color: var(--text-primary); margin: 0; }
.toast-desc  { color: var(--text-secondary); margin: 2px 0 0; }
.toast-dismiss { margin-left: auto; color: var(--text-tertiary); }
```

---

## Button Variants

```css
/* Primary */
.btn-primary {
  background: var(--action-primary);
  color: var(--action-primary-text);
  padding: 6px 14px;
  height: 32px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: background 120ms;
}
.btn-primary:hover { background: var(--action-primary-hover); }
.btn-primary:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
}
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }

/* Secondary */
.btn-secondary {
  background: var(--action-secondary);
  color: var(--text-primary);
  border: 1px solid var(--border-default);
  padding: 6px 14px;
  height: 32px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 450;
}
.btn-secondary:hover { background: var(--action-secondary-hover); }

/* Ghost (icon buttons, toolbars) */
.btn-ghost {
  background: transparent;
  color: var(--text-secondary);
  padding: 4px 8px;
  height: 28px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}
.btn-ghost:hover { background: var(--surface-hover); color: var(--text-primary); }
```

---

## Form Inputs

Always use `<label>` — never use placeholder as the only label.

```html
<div class="field">
  <label for="email" class="field-label">Email address</label>
  <input
    type="email"
    id="email"
    name="email"
    class="field-input"
    placeholder="you@example.com"
    autocomplete="email"
    aria-describedby="email-hint email-error"
  />
  <p id="email-hint" class="field-hint">We'll never share your email.</p>
  <p id="email-error" class="field-error" role="alert" hidden>
    Please enter a valid email address.
  </p>
</div>
```

```css
.field { display: flex; flex-direction: column; gap: 4px; }
.field-label { font-size: 13px; font-weight: 500; color: var(--text-primary); }
.field-input {
  height: 32px;
  padding: 0 10px;
  background: var(--bg-sunken);
  border: 1px solid var(--border-default);
  border-radius: 6px;
  font-size: 13px;
  color: var(--text-primary);
  outline: none;
  transition: border-color 120ms;
}
.field-input:hover  { border-color: var(--border-strong); }
.field-input:focus  { border-color: var(--border-focus); box-shadow: 0 0 0 2px rgba(var(--accent-rgb), 0.15); }
.field-hint  { font-size: 12px; color: var(--text-tertiary); margin: 0; }
.field-error { font-size: 12px; color: var(--status-error); margin: 0; }
```
