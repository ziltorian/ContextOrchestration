---
applyTo: '**'
name: 'Project_Documentation'
description: 'Documentation management rules.'
---

## Project Documentation Standards

### Documentation Management
- After any project change, add information about the change to documentation.
- Create a brief description (up to 5000 characters) in each module's `README.md`.
- Add a block about recent changes in the global `CHANGELOG.md`.
- Structure each `CHANGELOG.md` entry with fixed fields: date, scope, summary, affected files, and verification status.
- Write each `CHANGELOG.md` entry as a short standalone block so the change can be understood without reading git history.
- Use one canonical template for every `CHANGELOG.md` entry:
	```md
	### YYYY-MM-DD
	- Scope: ...
	- Summary: ...
	- Affected files: path1, path2, path3
	- Verification: ...
	```
- Create or update API documentation in `docs/api/*.md`.
- Create or update architecture documentation in `docs/architecture/*.md` based on actual codebase.
- Update specification in `docs/specification/*.md`.

### Specification Compliance
- Before changing documentation, review relevant specifications.
- Before reading documentation directly, use runSubagent to search for related and relevant data
- Use files in `docs/specification/*` as the main source of truth for project changes.

### File Requirements
- Documentation files must be 5000–15000 characters.
- Structure files in markdown format.
- Start each file with a "Table of Contents" section as links to chapters `[Topic 1](#topic-1)`
