# Implementation Planning Examples

Real-world examples demonstrating the complete workflow from planning to implementation.

## Example 1: Bug Fix - Pagination Detection

### Scenario

Pagination logic incorrectly detects last page, causing premature termination of data collection.

### Planning Phase

**Context gathering findings:**

- Current implementation uses single CSS selector for "next page" button
- Selector becomes disabled but stays in DOM
- No fallback detection mechanism
- Logging shows "Page 14/30" then stops

**Implementation plan created:**

**File: `.github/implementations/pagination_fix-implementation.instructions.md`**

```markdown
---
name: Pagination Detection Fix
description: Fix page detection logic to correctly identify last page using multiple indicators.
applyTo: "src/scraper/pagination.py"
tags: [bugfix, pagination]
version: "1.0.0"
---

## Goal

Fix pagination detection to accurately identify last page in result sets.

## Background

**Problem: Premature pagination termination**
- Symptom: Scraper stops at page 14 when 30 pages exist
- Symptom: Log shows "Page 14/30" then "Last page reached"
- Cause: `hasNextPage()` uses single selector that can be disabled but present

**Root cause:**
- Code: `return bool(soup.find('a', class_='next-page'))`
- Selector finds disabled element with same class
- No check for `disabled` attribute or aria-disabled

## Proposed Changes

### Scraper Module

#### [MODIFY] `pagination.py`
**Method:** `hasNextPage()` (lines 45-50)
- Add multiple detection strategies
- Check for disabled state
- Verify aria-disabled attribute
- Add page count validation

**Method:** `getCurrentPageInfo()` [NEW]
- Extract current page number
- Extract total page count
- Return structured data

#### [MODIFY] `pagination.py`
**Method:** `scrape_all_pages()` (lines 78-95)
- Use new detection strategies
- Add page count verification
- Improve error messages
- Log detailed pagination state

## Task

### Pagination Detection
- [ ] Refactor `hasNextPage()` to check disabled state <!-- id: P-1 -->
- [ ] Add aria-disabled attribute check <!-- id: P-2 -->
- [ ] Create `getCurrentPageInfo()` helper method <!-- id: P-3 -->
- [ ] Add page count validation logic <!-- id: P-4 -->

### Logging
- [ ] Add detailed pagination state logging <!-- id: L-1 -->
- [ ] Log current/total page numbers <!-- id: L-2 -->

### Error Handling
- [ ] Handle missing pagination elements gracefully <!-- id: E-1 -->
- [ ] Add timeout handling for page transitions <!-- id: E-2 -->

### Tests
- [ ] Create `test_pagination.py` with unit tests <!-- id: T-1 -->
- [ ] Add test for disabled button detection <!-- id: T-2 -->
- [ ] Add test for page count validation <!-- id: T-3 -->
- [ ] Add test for missing pagination elements <!-- id: T-4 -->

## Verification

**Unit tests:**
```bash
pytest tests/test_pagination.py -v
```

**Manual verification:**

1. Run scraper on dataset with 30 pages
2. Verify all pages collected
3. Check logs show accurate page counts
4. Test with disabled pagination buttons

**Expected results:**

- All 30 pages collected
- No premature termination
- Clear log messages showing "Page X/Y"

```

### Implementation Phase

**Task execution log:**

```markdown
## Changes Made

### Pagination Module (`src/scraper/pagination.py`)

#### `hasNextPage()` refactored (lines 45-63)
- Added disabled state check: `not element.has_attr('disabled')`
- Added aria-disabled check: `element.get('aria-disabled') != 'true'`
- Added href validation: `element.has_attr('href')`
- Implemented fallback strategies

#### `getCurrentPageInfo()` created (lines 65-75)
- Extracts current page from pagination info text
- Extracts total pages using regex pattern
- Returns dict: `{'current': int, 'total': int, 'has_next': bool}`

#### `scrape_all_pages()` updated (lines 90-120)
- Integrated page info extraction
- Added page count validation
- Improved error messages
- Enhanced logging with page numbers

### Tests (`tests/test_pagination.py`)
- Created comprehensive test suite (12 tests)
- Test cases:
  - `test_has_next_page_with_enabled_button()` ✓
  - `test_has_next_page_with_disabled_button()` ✓
  - `test_has_next_page_with_aria_disabled()` ✓
  - `test_has_next_page_missing_href()` ✓
  - `test_get_current_page_info_valid()` ✓
  - `test_get_current_page_info_last_page()` ✓
  - `test_scrape_all_pages_complete()` ✓
  - And 5 more edge case tests

### Verification Results

**Unit tests:** All 12 tests passing
```bash
pytest tests/test_pagination.py -v
================================ test session starts =================================
collected 12 items

tests/test_pagination.py::test_has_next_page_with_enabled_button PASSED       [ 8%]
tests/test_pagination.py::test_has_next_page_with_disabled_button PASSED      [16%]
...
================================ 12 passed in 2.34s =================================
```

**Manual testing:**

- Tested on 30-page dataset: ✓ All pages collected
- Log output shows accurate counts: ✓ "Page 14/30", "Page 15/30", etc.
- Disabled button handling: ✓ Correctly detects last page

```

**Tasks completed:**
```markdown
### Pagination Detection
- [x] Refactor `hasNextPage()` to check disabled state <!-- id: P-1 -->
- [x] Add aria-disabled attribute check <!-- id: P-2 -->
- [x] Create `getCurrentPageInfo()` helper method <!-- id: P-3 -->
- [x] Add page count validation logic <!-- id: P-4 -->

### Logging
- [x] Add detailed pagination state logging <!-- id: L-1 -->
- [x] Log current/total page numbers <!-- id: L-2 -->

### Error Handling
- [x] Handle missing pagination elements gracefully <!-- id: E-1 -->
- [x] Add timeout handling for page transitions <!-- id: E-2 -->

### Tests
- [x] Create `test_pagination.py` with unit tests <!-- id: T-1 -->
- [x] Add test for disabled button detection <!-- id: T-2 -->
- [x] Add test for page count validation <!-- id: T-3 -->
- [x] Add test for missing pagination elements <!-- id: T-4 -->
```

---

## Example 2: New Feature - OAuth 2.0 Authentication

### Scenario

Add OAuth 2.0 authentication to API, replacing current API key authentication.

### Planning Phase

**Context gathering findings:**

- Current auth: Simple API key in headers
- OAuth 2.0 requires: Token endpoint, refresh flow, session management
- Need to support multiple OAuth providers (Google, GitHub)
- Must maintain backward compatibility with API keys

**Implementation plan:**

**File: `.github/implementations/oauth-implementation.instructions.md`**

```markdown
---
name: OAuth 2.0 Authentication
description: Implement OAuth 2.0 authentication flow with token refresh and multi-provider support.
applyTo: "src/auth/** src/api/middleware/auth.py"
tags: [feature, security, authentication]
version: "1.0.0"
---

## Goal

Implement OAuth 2.0 authentication with support for multiple providers while maintaining API key backward compatibility.

## Background

**Current state:**
- API key authentication only
- Keys stored in database, passed in Authorization header
- No token refresh or expiration handling

**Requirements:**
- Support Google and GitHub OAuth providers
- Token-based authentication with refresh capability
- Maintain API key support for legacy clients
- Session management for web applications

## Proposed Changes

### Authentication Core

#### [NEW] `src/auth/oauth_client.py`
**Purpose:** OAuth 2.0 client implementation
**Contains:**
- `OAuthClient` - Base OAuth client class
- `GoogleOAuthClient(OAuthClient)` - Google-specific implementation
- `GitHubOAuthClient(OAuthClient)` - GitHub-specific implementation
- `create_oauth_client(provider)` - Factory function

#### [NEW] `src/auth/token_manager.py`
**Purpose:** Token storage and refresh management
**Contains:**
- `TokenManager` - Handle token storage, refresh, validation
- `TokenStore` - Database interface for tokens
- `refresh_token()` - Token refresh logic

#### [MODIFY] `src/auth/authenticator.py`
**Class:** `Authenticator` (lines 15-45)
- Add OAuth authentication method
- Integrate with OAuthClient
- Maintain API key fallback

### API Layer

#### [MODIFY] `src/api/middleware/auth.py`
**Function:** `authenticate_request()` (lines 30-55)
- Add OAuth token validation
- Check token expiration
- Trigger refresh if needed
- Maintain API key path

#### [NEW] `src/api/routes/auth.py`
**Purpose:** OAuth callback endpoints
**Contains:**
- `/auth/oauth/callback` - Handle OAuth callbacks
- `/auth/oauth/refresh` - Refresh token endpoint
- `/auth/oauth/revoke` - Token revocation

### Models

#### [NEW] `src/models/oauth_token.py`
**Purpose:** Token data model
**Contains:**
- `OAuthToken` - Token model with expiration, refresh
- Database migration for tokens table

#### [MODIFY] `src/models/user.py`
**Class:** `User` (lines 10-35)
- Add OAuth provider field
- Add OAuth provider user ID field
- Add relationship to tokens

### Configuration

#### [NEW] `src/config/oauth_config.py`
**Purpose:** OAuth provider configurations
**Contains:**
- Provider client IDs and secrets
- Redirect URIs
- Scope definitions

## Task

### Core OAuth Implementation
- [ ] Create `OAuthClient` base class <!-- id: O-1 -->
- [ ] Implement `GoogleOAuthClient` <!-- id: O-2 -->
- [ ] Implement `GitHubOAuthClient` <!-- id: O-3 -->
- [ ] Create provider factory function <!-- id: O-4 -->

### Token Management
- [ ] Create `TokenManager` class <!-- id: T-1 -->
- [ ] Implement token storage interface <!-- id: T-2 -->
- [ ] Implement token refresh logic <!-- id: T-3 -->
- [ ] Add token expiration checks <!-- id: T-4 -->

### API Integration
- [ ] Update authentication middleware <!-- id: A-1 -->
- [ ] Add OAuth callback endpoint <!-- id: A-2 -->
- [ ] Add token refresh endpoint <!-- id: A-3 -->
- [ ] Add token revocation endpoint <!-- id: A-4 -->

### Data Models
- [ ] Create `OAuthToken` model <!-- id: M-1 -->
- [ ] Create database migration for tokens <!-- id: M-2 -->
- [ ] Update `User` model for OAuth fields <!-- id: M-3 -->
- [ ] Create database migration for user updates <!-- id: M-4 -->

### Configuration
- [ ] Create OAuth configuration file <!-- id: C-1 -->
- [ ] Add environment variables for secrets <!-- id: C-2 -->
- [ ] Document configuration in README <!-- id: C-3 -->

### Tests
- [ ] Unit tests for `OAuthClient` classes <!-- id: TS-1 -->
- [ ] Unit tests for `TokenManager` <!-- id: TS-2 -->
- [ ] Integration tests for OAuth flow <!-- id: TS-3 -->
- [ ] Integration tests for token refresh <!-- id: TS-4 -->
- [ ] Test API key backward compatibility <!-- id: TS-5 -->

## User Review Required

> [!IMPORTANT]
> Which OAuth providers should we prioritize? Currently planning Google and GitHub. Should we also support Microsoft/Azure AD?

> [!WARNING]
> Implementing OAuth requires callback URLs to be registered with providers. This will need coordination with DevOps for production deployment.

## Verification

**Unit tests:**
```bash
pytest tests/auth/test_oauth_client.py -v
pytest tests/auth/test_token_manager.py -v
```

**Integration tests:**

```bash
pytest tests/integration/test_oauth_flow.py -v
```

**Manual verification:**

1. Start local server with OAuth configured
2. Navigate to `/auth/oauth/login?provider=google`
3. Complete Google OAuth flow
4. Verify token stored in database
5. Make authenticated API request with token
6. Wait for token expiration
7. Verify automatic token refresh
8. Test API key authentication still works

**Security checklist:**

- [ ] Secrets not committed to repository
- [ ] HTTPS required for OAuth endpoints
- [ ] State parameter prevents CSRF
- [ ] Tokens encrypted at rest

```

### Implementation Phase

(Similar execution log showing task completion, code changes, test results, and verification)

---

## Example 3: Refactoring - API Error Handling

### Scenario

Standardize error responses across all API endpoints using consistent format and HTTP status codes.

### Planning Phase

**File: `.github/implementations/api_error_refactor-implementation.instructions.md`**

```markdown
---
name: API Error Handling Standardization
description: Refactor API error handling to use consistent error response format and proper HTTP status codes.
applyTo: "src/api/**/*.py"
tags: [refactor, api, error-handling]
version: "1.0.0"
---

## Goal

Standardize error handling across all API endpoints with consistent response format and proper HTTP status codes.

## Background

**Current problems:**
- Inconsistent error response formats across endpoints
- Some endpoints return 200 OK with error in body
- Missing error details (no error codes, stack traces in production)
- No centralized error handling

**Examples of current inconsistency:**
```json
// Endpoint A returns:
{"error": "Not found"}

// Endpoint B returns:
{"message": "Resource not found", "status": "error"}

// Endpoint C returns:
{"success": false, "error_message": "Not found"}
```

**Desired standard format:**

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested resource was not found",
    "details": {
      "resource_type": "user",
      "resource_id": "12345"
    },
    "timestamp": "2026-02-07T10:30:00Z"
  }
}
```

## Proposed Changes

### Error Framework

#### [NEW] `src/api/errors/exceptions.py`

**Purpose:** Custom exception classes
**Contains:**

- `APIError` - Base exception with error code and details
- `ValidationError(APIError)` - 400 errors
- `AuthenticationError(APIError)` - 401 errors
- `AuthorizationError(APIError)` - 403 errors
- `NotFoundError(APIError)` - 404 errors
- `ConflictError(APIError)` - 409 errors
- `ServerError(APIError)` - 500 errors

#### [NEW] `src/api/errors/error_codes.py`

**Purpose:** Enum of all error codes
**Contains:**

- `ErrorCode(Enum)` - All possible error codes
- Error code to HTTP status mapping

#### [NEW] `src/api/errors/handlers.py`

**Purpose:** Global error handlers
**Contains:**

- `handle_api_error()` - Format APIError to JSON
- `handle_validation_error()` - Format validation errors
- `handle_unexpected_error()` - Handle uncaught exceptions

### API Integration

#### [MODIFY] All route files in `src/api/routes/`

**Changes across all endpoints:**

- Replace string error returns with exception raises
- Use appropriate exception types
- Include error details where helpful
- Remove try/catch blocks handling formatting

**Example files:**

- `src/api/routes/users.py` (15 endpoints)
- `src/api/routes/auth.py` (8 endpoints)
- `src/api/routes/data.py` (12 endpoints)

#### [MODIFY] `src/api/app.py`

**Function:** `create_app()` (lines 25-45)

- Register global error handlers
- Add error logging middleware
- Configure error response format

### Validation

#### [MODIFY] `src/api/validators/request_validator.py`

**Class:** `RequestValidator` (lines 30-80)

- Raise `ValidationError` instead of returning error dict
- Include field-level error details
- Use error codes from ErrorCode enum

## Task

### Error Framework

- [ ] Create `APIError` exception hierarchy <!-- id: E-1 -->
- [ ] Create `ErrorCode` enum with all codes <!-- id: E-2 -->
- [ ] Create global error handlers <!-- id: E-3 -->
- [ ] Add error logging middleware <!-- id: E-4 -->

### Route Refactoring - Users

- [ ] Refactor `GET /users` endpoint <!-- id: U-1 -->
- [ ] Refactor `POST /users` endpoint <!-- id: U-2 -->
- [ ] Refactor `GET /users/:id` endpoint <!-- id: U-3 -->
- [ ] Refactor remaining 12 user endpoints <!-- id: U-4 -->

### Route Refactoring - Auth

- [ ] Refactor all 8 auth endpoints <!-- id: A-1 -->

### Route Refactoring - Data

- [ ] Refactor all 12 data endpoints <!-- id: D-1 -->

### Validation

- [ ] Update `RequestValidator` to use new exceptions <!-- id: V-1 -->
- [ ] Update all validation schemas <!-- id: V-2 -->

### Tests

- [ ] Unit tests for error exceptions <!-- id: T-1 -->
- [ ] Unit tests for error handlers <!-- id: T-2 -->
- [ ] Integration tests for each endpoint <!-- id: T-3 -->
- [ ] Test error response format consistency <!-- id: T-4 -->

### Documentation

- [ ] Document error codes in API docs <!-- id: DOC-1 -->
- [ ] Update OpenAPI/Swagger spec <!-- id: DOC-2 -->
- [ ] Create error handling guide for developers <!-- id: DOC-3 -->

## Verification

**Unit tests:**

```bash
pytest tests/api/errors/ -v
pytest tests/api/validators/ -v
```

**Integration tests:**

```bash
pytest tests/integration/test_error_responses.py -v
```

**Manual verification:**

1. Trigger each error type (404, 400, 401, 403, 500)
2. Verify consistent response format
3. Check HTTP status codes are correct
4. Verify error codes in responses
5. Test error logging is working

**API contract verification:**

- All error responses follow standard format
- No 200 OK responses with errors in body
- Error codes documented in API docs

```

---

## Example 4: Multi-File Refactoring

This example demonstrates handling a large refactoring that touches many files.

### Key Patterns Demonstrated

1. **Breaking into components** - Group related files
2. **Task granularity** - Balance between too detailed and too vague
3. **Phased implementation** - Core framework first, then migration
4. **Progress tracking** - Track completion across multiple components

---

## Common Patterns

### Pattern 1: Research Before Planning

**Good:**
```

User: Fix the login bug
Agent:

  1. Read login code in auth module
  2. Search for error logs related to login
  3. Review authentication flow documentation
  4. Check recent changes to auth system
  5. [After research] Create implementation plan

```

**Bad:**
```

User: Fix the login bug
Agent: [Immediately creates plan without understanding the bug]

```

### Pattern 2: Atomic Tasks

**Good:**
```markdown
- [ ] Add null check to validate_input() method <!-- id: V-1 -->
- [ ] Create ValidationResult dataclass <!-- id: V-2 -->
- [ ] Update error messages in validation module <!-- id: V-3 -->
```

**Bad:**

```markdown
- [ ] Improve validation with better error handling <!-- id: V-1 -->
```

### Pattern 3: Progress Communication

**Good:**

```markdown
### Validation
- [x] Add null check to validate_input() <!-- id: V-1 -->
- [/] Create ValidationResult dataclass <!-- id: V-2 -->
      ^ Currently investigating dataclass vs Pydantic model
- [ ] Update error messages <!-- id: V-3 -->
```

**Bad:**

```markdown
### Validation
- [ ] All validation tasks <!-- id: V-1 -->
[No status updates, user doesn't know progress]
```

### Pattern 4: Verification Before Completion

**Good:**

```markdown
## Verification Results

**Unit tests:** 15/15 passing
**Integration tests:** 8/8 passing
**Manual testing:**
- Login with valid credentials: ✓ Works
- Login with invalid password: ✓ Proper error message
- Login with non-existent user: ✓ Proper error message
```

**Bad:**

```markdown
## Verification

All tests passed.
```

---

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Vague Goals

**Bad:**

```markdown
## Goal
Make the code better and fix some issues.
```

**Good:**

```markdown
## Goal
Fix pagination detection to correctly identify last page using multiple indicators.

## Background
**Problem:** Scraper stops prematurely at page 14 of 30
- Symptom: `hasNextPage()` returns false while pages remain
- Cause: Disabled button still present in DOM
```

### ❌ Anti-Pattern 2: Code in Proposed Changes

**Bad:**

```markdown
## Proposed Changes

### [MODIFY] `auth.py`
```python
def authenticate(token):
    if not token:
        raise ValueError("Token required")
    return validate_token(token)
```

```

**Good:**
```markdown
## Proposed Changes

### Authentication Module

#### [MODIFY] `auth.py`
**Function:** `authenticate()` (line 45)
- Add token presence validation
- Raise `AuthenticationError` for missing token
- Call `validate_token()` for validation
```

### ❌ Anti-Pattern 3: Duplicate Tasks

**Bad:**

```markdown
## Task
- [ ] Create validation tests <!-- id: T-1 -->
- [ ] Write unit tests for validation <!-- id: T-2 -->
- [ ] Create validation tests <!-- id: T-1 --> <!-- DUPLICATE! -->
```

**Good:**

```markdown
## Task
- [ ] Create `test_validation.py` with unit tests <!-- id: T-1 -->
- [ ] Create `test_api_validation.py` with integration tests <!-- id: T-2 -->
```

---

## Summary

These examples demonstrate:

1. **Complete workflow** - From research to verification
2. **Proper structure** - Following the documented format
3. **Task granularity** - Atomic, actionable tasks
4. **Progress tracking** - Real-time status updates
5. **Verification** - Comprehensive testing before completion

Use these as templates for your own implementation planning workflows.
