# API Endpoints

## Base URL

```
{e.g., http://localhost:8000/api/v1}
```

## Authentication

{Describe authentication method: Bearer token, API key, etc.}

## Endpoints

### {Resource Name}

#### `GET /resource`

**Description:** {What this endpoint returns}

**Response:**
```json
{
  "items": [],
  "total": 0
}
```

#### `POST /resource`

**Description:** {What this endpoint creates}

**Request body:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Response:** `201 Created`
```json
{
  "id": "string",
  "name": "string"
}
```

## Error Handling

All errors follow this format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable description"
  }
}
```

| Status | Code | Description |
|--------|------|-------------|
| 400 | `VALIDATION_ERROR` | Invalid request body |
| 401 | `UNAUTHORIZED` | Missing or invalid token |
| 404 | `NOT_FOUND` | Resource does not exist |
| 500 | `INTERNAL_ERROR` | Unexpected server error |
