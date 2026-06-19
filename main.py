#!/usr/bin/env python3
"""
Lobster AI Assistant - Main Entry Point

Your personal AI. Your device. Your control.
"""

import asyncio
import sys
from pathlib import Path
from loguru import logger

from core.assistant import LobsterAssistant
from integrations.server import start_server

# Configure logging
logger.remove()
logger.add(
    sys.stderr,
    format="<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
    level="INFO"
)


class LobsterApp:
    """Main application class for Lobster AI Assistant."""

    def __init__(self):
        self.assistant = None
        self.config = None

    async def initialize(self):
        """Initialize the assistant and all integrations."""
        logger.info("🦞 Initializing Lobster AI Assistant...")
        
        try:
            # Load configuration
            from core.config import load_config
            self.config = load_config()
            logger.info(f"✓ Configuration loaded")
            
            # Initialize core assistant
            self.assistant = LobsterAssistant(self.config)
            await self.assistant.initialize()
            logger.info("✓ Core AI engine initialized")
            
            # Initialize integrations
            await self._setup_integrations()
            
            logger.info("✓ All systems ready!")
            return True
            
        except Exception as e:
            logger.error(f"✗ Initialization failed: {e}")
            return False

    async def _setup_integrations(self):
        """Setup chat and voice integrations based on config."""
        logger.info("Setting up integrations...")
        
        integrations = self.config.get('integrations', {})
        
        if integrations.get('whatsapp', {}).get('enabled'):
            from integrations.whatsapp import WhatsAppConnector
            logger.info("  → WhatsApp integration enabled")
            
        if integrations.get('discord', {}).get('enabled'):
            from integrations.discord import DiscordConnector
            logger.info("  → Discord integration enabled")
            
        if integrations.get('telegram', {}).get('enabled'):
            from integrations.telegram import TelegramConnector
            logger.info("  → Telegram integration enabled")
            
        if integrations.get('slack', {}).get('enabled'):
            from integrations.slack import SlackConnector
            logger.info("  → Slack integration enabled")

    async def run(self):
        """Start the assistant server and all integrations."""
        if not await self.initialize():
            sys.exit(1)
        
        logger.info("\n" + "="*50)
        logger.info("🦞 Lobster AI Assistant is running!")
        logger.info("="*50)
        logger.info(f"Web Interface: http://127.0.0.1:8000")
        logger.info(f"Documentation: http://127.0.0.1:8000/docs")
        logger.info("\nPress Ctrl+C to stop\n")
        
        try:
            await start_server(self.assistant, self.config)
        except KeyboardInterrupt:
            logger.info("\n🦞 Shutting down gracefully...")
            await self.shutdown()

    async def shutdown(self):
        """Cleanup and shutdown."""
        if self.assistant:
            await self.assistant.cleanup()
        logger.info("✓ Goodbye! 👋")


def main():
    """Entry point."""
    app = LobsterApp()
    try:
        asyncio.run(app.run())
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
