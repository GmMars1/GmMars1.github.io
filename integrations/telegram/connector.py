"""Telegram connector for Lobster Assistant."""

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters
from loguru import logger
from typing import Optional


class TelegramConnector:
    """Connect Lobster to Telegram."""

    def __init__(self, config: dict, assistant):
        self.config = config
        self.assistant = assistant
        self.app = None

    async def initialize(self):
        """Initialize Telegram connection."""
        logger.info("Initializing Telegram connector...")
        
        token = self.config.get('token')
        if not token:
            logger.error("Telegram token not found in config")
            return
        
        self.app = Application.builder().token(token).build()
        
        # Add message handler
        self.app.add_handler(MessageHandler(filters.TEXT, self._handle_message))
        
        logger.info("✓ Telegram connector ready")

    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming Telegram message."""
        message = update.message.text
        user_id = str(update.message.from_user.id)
        
        response = await self.assistant.process_message(message, user_id)
        await update.message.reply_text(f"🦞 {response}")

    async def start(self):
        """Start the Telegram bot."""
        if self.app:
            await self.app.run_polling()
