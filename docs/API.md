# Lobster AI Assistant API Reference

## REST API Endpoints

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "assistant": "Lobster"
}
```

---

### Send Message

```http
POST /message
Content-Type: application/json

{
  "user_id": "user123",
  "message": "What's the weather like?"
}
```

**Response:**
```json
{
  "response": "🦞 I'm a local AI, so I can't check the weather. But I can help you with many other things!",
  "user_id": "user123"
}
```

---
## Error Handling

```json
{
  "detail": "Error message here",
  "status_code": 500
}
```

**Common errors:**
- `400 Bad Request`: Invalid message format
- `500 Internal Server Error`: Processing error
- `422 Unprocessable Entity`: Missing or invalid JSON fields

---

## Implemented Endpoint Summary

Current FastAPI server implementation exposes:
- `GET /`
- `GET /health`
- `POST /message`

This repository does not currently include a Python SDK, WebSocket endpoint, or streaming `/message/stream` endpoint.
