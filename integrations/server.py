"""FastAPI server for Lobster Assistant."""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict
from loguru import logger


class MessageRequest(BaseModel):
    user_id: str
    message: str


class MessageResponse(BaseModel):
    response: str
    user_id: str


async def start_server(assistant, config: Dict):
    """Start the FastAPI server."""
    app = FastAPI(title="Lobster AI Assistant", version="1.0.0")

    @app.get("/", response_class=HTMLResponse)
    async def root():
        """Web interface."""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>🦞 Lobster AI Assistant</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; }
                .container { background: #f5f5f5; padding: 20px; border-radius: 10px; }
                h1 { color: #e74c3c; }
                input { width: 100%; padding: 10px; margin: 10px 0; }
                button { padding: 10px 20px; background: #e74c3c; color: white; border: none; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🦞 Lobster AI Assistant</h1>
                <p>Your personal AI. Your device. Your control.</p>
                <input type="text" id="message" placeholder="Message your assistant...">
                <button onclick="sendMessage()">Send</button>
                <div id="response" style="margin-top: 20px; padding: 10px; background: white;"></div>
            </div>
            <script>
                async function sendMessage() {
                    const message = document.getElementById('message').value;
                    if (!message) return;
                    
                    const response = await fetch('/message', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({user_id: 'web-user', message: message})
                    });
                    
                    const data = await response.json();
                    document.getElementById('response').innerHTML = `<strong>🦞:</strong> ${data.response}`;
                    document.getElementById('message').value = '';
                }
            </script>
        </body>
        </html>
        """

    @app.post("/message", response_model=MessageResponse)
    async def process_message(request: MessageRequest):
        """Process a message and return a response."""
        try:
            response = await assistant.process_message(request.message, request.user_id)
            return MessageResponse(response=response, user_id=request.user_id)
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/health")
    async def health():
        """Health check endpoint."""
        return {"status": "healthy", "assistant": "Lobster"}

    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
