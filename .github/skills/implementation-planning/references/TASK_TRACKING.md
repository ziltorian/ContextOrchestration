# Task Tracking Guide

Advanced patterns for managing implementation tasks across complex projects.

## Task Status System

The skill uses markdown checkboxes with three states to track progress:

```markdown
- [ ] Not started - Task has not been begun
- [/] In progress - Currently working on task, or investigating blocker
- [x] Completed - Task successfully finished and verified
```

## Task ID System

Each task must have a unique identifier for tracking and reference:

```markdown
- [ ] Task description <!-- id: COMPONENT-NUMBER -->
```

**Format rules:**

- `COMPONENT` - Short component identifier (2-4 characters)
- `NUMBER` - Sequential number within component
- Use format: `C1-1`, `API-3`, `TEST-5`

**Examples:**

```markdown
- [ ] Add validation logic <!-- id: V-1 -->
- [ ] Create user model <!-- id: M-1 -->
- [ ] Write API tests <!-- id: T-1 -->
```

## Task Organization Patterns

### Pattern 1: Component-Based Organization

Group tasks by the component or module they affect:

```markdown
## Task

### Core Module
- [ ] Refactor authentication logic <!-- id: C-1 -->
- [ ] Add session management <!-- id: C-2 -->
- [ ] Implement token refresh <!-- id: C-3 -->

### API Layer
- [ ] Update authentication middleware <!-- id: A-1 -->
- [ ] Add OAuth endpoints <!-- id: A-2 -->

### Tests
- [ ] Unit tests for auth module <!-- id: T-1 -->
- [ ] Integration tests for OAuth flow <!-- id: T-2 -->
```

**When to use:**

- Medium to large implementations
- Changes span multiple components
- Clear component boundaries exist

### Pattern 2: Workflow-Based Organization

Group tasks by the workflow or process they implement:

```markdown
## Task

### Setup Phase
- [ ] Create database schema <!-- id: S-1 -->
- [ ] Configure OAuth providers <!-- id: S-2 -->
- [ ] Set up environment variables <!-- id: S-3 -->

### Implementation Phase
- [ ] Implement OAuth client <!-- id: I-1 -->
- [ ] Create token manager <!-- id: I-2 -->
- [ ] Add API endpoints <!-- id: I-3 -->

### Testing Phase
- [ ] Write unit tests <!-- id: T-1 -->
- [ ] Write integration tests <!-- id: T-2 -->
- [ ] Manual testing <!-- id: T-3 -->
```

**When to use:**

- Sequential dependencies between tasks
- Clear implementation phases
- Setup/implementation/verification pattern

### Pattern 3: Priority-Based Organization

Group tasks by priority or urgency:

```markdown
## Task

### Critical (Must have)
- [ ] Fix authentication bug <!-- id: P1-1 -->
- [ ] Add data validation <!-- id: P1-2 -->
- [ ] Implement error handling <!-- id: P1-3 -->

### Important (Should have)
- [ ] Add logging <!-- id: P2-1 -->
- [ ] Improve error messages <!-- id: P2-2 -->

### Nice to have
- [ ] Add telemetry <!-- id: P3-1 -->
- [ ] Optimize performance <!-- id: P3-2 -->
```

**When to use:**

- Time-constrained implementations
- Incremental delivery needed
- Stakeholder review required

## Task Granularity Guidelines

### Atomic Task Definition

Each task should represent a single, clear action that can be completed independently.

**Good granularity:**

```markdown
- [ ] Add null check to validate_input() method <!-- id: V-1 -->
- [ ] Create ValidationResult dataclass in validators.py <!-- id: V-2 -->
- [ ] Update error messages in validation module <!-- id: V-3 -->
- [ ] Add unit test for null validation <!-- id: T-1 -->
```

**Too granular:**

```markdown
- [ ] Import dataclass from dataclasses <!-- id: V-1 -->
- [ ] Create ValidationResult class <!-- id: V-2 -->
- [ ] Add is_valid field to ValidationResult <!-- id: V-3 -->
- [ ] Add errors field to ValidationResult <!-- id: V-4 -->
- [ ] Add warnings field to ValidationResult <!-- id: V-5 -->
```

**Too vague:**

```markdown
- [ ] Improve validation <!-- id: V-1 -->
- [ ] Add tests <!-- id: T-1 -->
```

### Task Size Estimation

**Good task size:** 15-60 minutes of focused work

**Too small:** < 10 minutes (consider combining)
**Too large:** > 2 hours (consider splitting)

### File-Based Task Scope

**Single file change:**

```markdown
- [ ] Add authentication to user routes in routes/users.py <!-- id: R-1 -->
```

**Multiple related files:**

```markdown
- [ ] Create user model (models/user.py) and migration (migrations/001_users.sql) <!-- id: M-1 -->
```

**Avoid cross-module mega-tasks:**

```markdown
❌ - [ ] Implement authentication across all modules <!-- id: A-1 -->

✅ Split into:
- [ ] Implement auth module (auth/authenticator.py) <!-- id: A-1 -->
- [ ] Add auth middleware (api/middleware/auth.py) <!-- id: A-2 -->
- [ ] Update user routes (api/routes/users.py) <!-- id: A-3 -->
```

## Progress Tracking Patterns

### Pattern 1: Sequential Execution

Mark tasks in progress as you work through them:

```markdown
### API Implementation
- [x] Create user endpoint <!-- id: A-1 -->
- [x] Add validation <!-- id: A-2 -->
- [/] Implement authentication <!-- id: A-3 --> Currently working
- [ ] Add error handling <!-- id: A-4 -->
- [ ] Add rate limiting <!-- id: A-5 -->
```

### Pattern 2: Parallel Execution

Mark multiple tasks in progress when working on independent components:

```markdown
### Frontend
- [/] Create login form component <!-- id: F-1 --> In progress
- [ ] Add form validation <!-- id: F-2 -->

### Backend
- [/] Implement auth endpoint <!-- id: B-1 --> In progress
- [ ] Add session management <!-- id: B-2 -->
```

### Pattern 3: Blocked Task Tracking

Use `[/]` with notes for blocked tasks:

```markdown
### Database
- [x] Create schema <!-- id: D-1 -->
- [/] Run migration <!-- id: D-2 -->
     ^ Blocked: Waiting for DBA approval
- [ ] Seed test data <!-- id: D-3 -->

### API
- [/] Add user endpoints <!-- id: A-1 -->
     ^ Blocked: Needs user schema from D-2
```

## Handling Task Changes

### Adding New Tasks

When discovering additional work during implementation:

```markdown
## Task

### Original Tasks
- [x] Implement login function <!-- id: A-1 -->
- [/] Add session management <!-- id: A-2 -->

### Newly Discovered Tasks
- [ ] Add CSRF token validation <!-- id: A-3 --> ADDED: Required for security
- [ ] Implement session timeout <!-- id: A-4 --> ADDED: Not in original plan
```

**Document additions:**

- Mark as "ADDED" with reason
- Update task IDs to maintain sequence
- Add to appropriate component section

### Removing Tasks

When tasks become unnecessary:

```markdown
## Task

### Authentication
- [x] Implement JWT tokens <!-- id: A-1 -->
- ~~Add session cookies~~ <!-- id: A-2 --> REMOVED: Using JWT instead
- [x] Add token refresh <!-- id: A-3 -->
```

**Document removals:**

- Use strikethrough (~~text~~)
- Keep ID for reference
- Note reason for removal

### Splitting Tasks

When a task proves too large:

```markdown
## Task

### Original
- ~~Implement OAuth flow~~ <!-- id: O-1 --> SPLIT into O-1a, O-1b, O-1c

### Split Tasks
- [x] Implement OAuth client <!-- id: O-1a -->
- [/] Implement token storage <!-- id: O-1b -->
- [ ] Implement token refresh <!-- id: O-1c -->
```

## Verification Checkpoints

Add verification sub-tasks for quality gates:

```markdown
## Task

### Implementation
- [x] Create pagination logic <!-- id: P-1 -->
- [x] Add page validation <!-- id: P-2 -->
- [x] Write unit tests <!-- id: T-1 -->

### Verification Checkpoint
- [x] All unit tests pass <!-- id: V-1 -->
- [x] Manual testing complete <!-- id: V-2 -->
- [x] Code review passed <!-- id: V-3 -->

### Deployment
- [ ] Update documentation <!-- id: D-1 -->
- [ ] Deploy to staging <!-- id: D-2 -->
```

## Task Dependencies

### Explicit Dependencies

Document dependencies in task descriptions:

```markdown
## Task

### Setup
- [ ] Create database schema <!-- id: S-1 -->

### Models (depends on S-1)
- [ ] Create user model <!-- id: M-1 --> Requires: S-1
- [ ] Create session model <!-- id: M-2 --> Requires: S-1

### API (depends on M-1, M-2)
- [ ] Implement user endpoints <!-- id: A-1 --> Requires: M-1
- [ ] Implement auth endpoints <!-- id: A-2 --> Requires: M-1, M-2
```

### Implicit Dependencies

Use component organization to imply dependencies:

```markdown
## Task

### Phase 1: Foundation
- [ ] Core module setup <!-- id: P1-1 -->
- [ ] Database schema <!-- id: P1-2 -->

### Phase 2: Implementation (requires Phase 1 complete)
- [ ] Business logic <!-- id: P2-1 -->
- [ ] API layer <!-- id: P2-2 -->

### Phase 3: Testing (requires Phase 2 complete)
- [ ] Unit tests <!-- id: P3-1 -->
- [ ] Integration tests <!-- id: P3-2 -->
```

## Progress Reporting

### Daily Progress Updates

Track what was completed each session:

```markdown
## Progress Log

### 2026-02-07
- [x] Completed tasks: A-1, A-2, T-1
- [/] In progress: A-3 (70% complete)
- Blockers: None
- Next session: Complete A-3, start A-4

### 2026-02-06
- [x] Completed tasks: P-1, P-2
- Issues found: Pagination bug (fixed)
- Added tasks: A-3 (security requirement)
```

### Completion Percentage

Calculate overall progress:

```markdown
## Task Summary

**Total tasks:** 24
**Completed:** 18 (75%)
**In progress:** 2 (8%)
**Not started:** 4 (17%)

**By component:**
- Core Module: 8/8 (100%) ✓
- API Layer: 6/10 (60%)
- Tests: 4/6 (67%)
```

## Advanced Patterns

### Pattern 1: Sub-tasks

Use indentation for sub-tasks:

```markdown
## Task

### Authentication
- [x] Implement OAuth flow <!-- id: A-1 -->
  - [x] Create OAuth client <!-- id: A-1a -->
  - [x] Add callback handler <!-- id: A-1b -->
  - [x] Implement token exchange <!-- id: A-1c -->
- [ ] Add token refresh <!-- id: A-2 -->
  - [ ] Create refresh logic <!-- id: A-2a -->
  - [ ] Add expiration handling <!-- id: A-2b -->
```

### Pattern 2: Conditional Tasks

Mark tasks that depend on decisions:

```markdown
## Task

### Core Implementation
- [x] Basic authentication <!-- id: A-1 -->

### Optional Features (pending user decision)
- [ ] Add OAuth support <!-- id: O-1 --> IF: User approves OAuth
- [ ] Add LDAP support <!-- id: L-1 --> IF: Enterprise tier
- [ ] Add SAML support <!-- id: S-1 --> IF: Enterprise tier
```

### Pattern 3: Rollback Tasks

Plan for rollback if implementation fails:

```markdown
## Task

### Implementation
- [x] Deploy new auth system <!-- id: D-1 -->
- [x] Monitor for errors <!-- id: D-2 -->

### Rollback (if needed)
- [ ] Revert database migration <!-- id: R-1 -->
- [ ] Switch back to old auth <!-- id: R-2 -->
- [ ] Notify users <!-- id: R-3 -->
```

## Integration with Tools

### VS Code Task Integration

Tasks can be tracked in VS Code:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Show Implementation Tasks",
      "type": "shell",
      "command": "grep -r '\\[ \\]\\|\\[/\\]\\|\\[x\\]' .github/implementations/",
      "problemMatcher": []
    }
  ]
}
```

### Git Integration

Reference task IDs in commits:

```bash
git commit -m "feat: Add OAuth client [A-1]"
git commit -m "test: Add auth tests [T-1, T-2]"
git commit -m "fix: Handle token expiration [A-3]"
```

### Issue Tracking Integration

Link tasks to issues:

```markdown
## Task

### Bug Fixes
- [x] Fix pagination (#123) <!-- id: B-1 -->
- [ ] Fix auth timeout (#124) <!-- id: B-2 -->

### Features
- [ ] Add OAuth (#125) <!-- id: F-1 -->
```

## Best Practices Summary

**DO:**

- ✅ Keep tasks atomic and focused
- ✅ Use unique IDs for each task
- ✅ Update status in real-time
- ✅ Document blockers clearly
- ✅ Add newly discovered tasks
- ✅ Group related tasks
- ✅ Verify before marking complete

**DON'T:**

- ❌ Create duplicate tasks
- ❌ Make tasks too vague
- ❌ Skip status updates
- ❌ Hide blockers
- ❌ Mark incomplete tasks as done
- ❌ Mix unrelated tasks
- ❌ Forget verification steps

## Summary

Effective task tracking requires:

1. **Clear task definitions** - Atomic, actionable, specific
2. **Consistent status updates** - Real-time progress tracking
3. **Logical organization** - Component, workflow, or priority-based
4. **Dependency awareness** - Understanding task relationships
5. **Progress visibility** - Regular updates and reporting
6. **Flexibility** - Adapting to discoveries and changes
