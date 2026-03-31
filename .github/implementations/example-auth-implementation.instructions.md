---
name: User Authentication Implementation
description: Example implementation plan demonstrating the standard format. Replace with your actual task.
applyTo: "src/auth/**"
---

# User Authentication Implementation

> **This is an example plan.** Copy this file as a starting template for your own implementation plans. Delete this notice in your copy.

## Goal

Add JWT-based user authentication to the REST API so that protected endpoints require a valid token.

## Background

**Observed symptoms:**
- All API endpoints are publicly accessible without authentication
- No user model or session management exists

**Root cause:**
- Authentication was deferred during initial scaffolding (Phase 1)
- The project has no auth middleware or user storage

## Phases

**Phase 1: Minimum viable** — user registration, login, JWT token issuance  
**Phase 2: Core experience** — auth middleware, protected routes, token refresh  
**Phase 3: Edge cases** — rate limiting, password reset, account lockout  

## Proposed Changes

### Auth Module

#### [NEW] `src/auth/models.py`
**Purpose:** User model and password hashing utilities  
**Contains:**
- `User` — SQLAlchemy model with email, hashed_password, created_at
- `hash_password()` — bcrypt wrapper
- `verify_password()` — bcrypt verification  
**Why:** Foundation for all auth operations  
**Risk:** Low

#### [NEW] `src/auth/jwt.py`
**Purpose:** JWT token creation and validation  
**Contains:**
- `create_access_token()` — generates signed JWT
- `decode_token()` — validates and decodes JWT  
**Why:** Stateless authentication mechanism  
**Risk:** Medium — incorrect implementation creates security vulnerabilities

#### [NEW] `src/auth/router.py`
**Purpose:** Auth API endpoints  
**Contains:**
- `POST /auth/register` — create new user
- `POST /auth/login` — authenticate and return token  
**Why:** User-facing auth interface  
**Risk:** Low

#### [MODIFY] `src/api/middleware.py`
**Method:** `process_request()` (lines 15-30)  
**Changes:**
- Add JWT validation for routes marked as protected
- Return 401 for missing/invalid tokens  
**Why:** Without this, protected endpoints remain publicly accessible  
**Risk:** Medium — affects all existing routes

### Database

#### [NEW] `migrations/003_add_users_table.sql`
**Purpose:** Create users table  
**Why:** User storage required before any auth logic  
**Risk:** Low

## Task

### Phase 1 — Auth Module
- [ ] Create User model with password hashing <!-- id: C1-1 -->
- [ ] Implement JWT create/decode utilities <!-- id: C1-2 -->
- [ ] Add registration endpoint <!-- id: C1-3 -->
- [ ] Add login endpoint <!-- id: C1-4 -->
- [ ] Create users table migration <!-- id: C1-5 -->

### Phase 2 — Middleware
- [ ] Add auth middleware to validate JWT on protected routes <!-- id: C2-1 -->
- [ ] Mark existing endpoints as protected/public <!-- id: C2-2 -->
- [ ] Add token refresh endpoint <!-- id: C2-3 -->

### Tests
- [ ] Unit tests for password hashing and JWT utilities <!-- id: T-1 -->
- [ ] Integration tests for register/login flow <!-- id: T-2 -->
- [ ] Test 401 response for missing/invalid tokens <!-- id: T-3 -->

## Testing Strategy

**Unit tests:**
- `test_jwt.py` — token creation, expiry, invalid signature
- `test_models.py` — password hash/verify, user creation

**Integration tests:**
- Full auth flow: register → login → access protected route → token refresh
- Invalid credentials: wrong password, non-existent user

**Manual verification:**
1. Register a new user via API
2. Login and receive JWT
3. Access protected endpoint with token → 200
4. Access protected endpoint without token → 401

## Success Criteria

- [ ] Users can register and login via API
- [ ] Protected endpoints reject unauthenticated requests
- [ ] JWT tokens expire after configured TTL
- [ ] Passwords are stored hashed, never in plaintext
- [ ] All tests pass

## Risks & Mitigations

- **Risk:** JWT secret key hardcoded in source
  - Mitigation: Load from environment variable, fail on startup if missing
- **Risk:** Auth middleware breaks existing endpoints
  - Mitigation: Default to public; explicitly opt-in routes to protection in Phase 2
- **Risk:** Password hashing too slow in tests
  - Mitigation: Use reduced bcrypt rounds in test configuration
