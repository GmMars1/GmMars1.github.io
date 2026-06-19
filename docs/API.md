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

## Python SDK

```python
from lobster.client import LobsterClient

# Connect to local Lobster
client = LobsterClient("http://localhost:8000")

# Send message
response = client.send_message(
    user_id="user123",
    message="What can you help me with?"
)

print(response)  # 🦞 I can help with...
```

---

## WebSocket (Real-time)

```python
import asyncio
from lobster.client import LobsterWebSocketClient

async def main():
    client = await LobsterWebSocketClient("ws://localhost:8000/ws")
    
    # Send message
    await client.send_message(
        user_id="user123",
        message="Stream this response"
    )
    
    # Receive streaming response
    async for chunk in client.receive():
        print(chunk, end="", flush=True)

asyncio.run(main())
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
- `503 Service Unavailable`: LLM not ready

---

## Rate Limiting

No rate limits for local deployment. Use as much as you want!

---

## Streaming Responses

For long responses, use streaming to get chunks as they're generated:

```http
POST /message/stream
Content-Type: application/json

{"user_id": "user123", "message": "Tell me a story"}
```

The response will stream tokens as they're generated.
