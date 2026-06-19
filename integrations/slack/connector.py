"""Slack connector for Lobster Assistant."""

from slack_bolt import App
from slack_bolt.context import BoltContext
from loguru import logger
from typing import Optional


class SlackConnector:
    """Connect Lobster to Slack."""

    def __init__(self, config: dict, assistant):
        self.config = config
        self.assistant = assistant
        self.app = None

    async def initialize(self):
        """Initialize Slack connection."""
        logger.info("Initializing Slack connector...")
        
        token = self.config.get('bot_token')
        signing_secret = self.config.get('signing_secret')
        
        if not token or not signing_secret:
            logger.error("Slack credentials not found in config")
            return
        
        self.app = App(token=token, signing_secret=signing_secret)
        
        @self.app.message(".*")
        async def handle_message(body, say, context: BoltContext):
            message = body['event']['text']
            user_id = body['event']['user']
            
            response = await self.assistant.process_message(message, user_id)
            say(f"🦞 {response}")
        
        logger.info("✓ Slack connector ready")

    async def start(self):
        """Start the Slack app."""
        if self.app:
            handler = await self.app.async_listener_runner()
            await handler()
