"""Discord connector for Lobster Assistant."""

import discord
from discord.ext import commands
from loguru import logger
from typing import Optional


class DiscordConnector:
    """Connect Lobster to Discord."""

    def __init__(self, config: dict, assistant):
        self.config = config
        self.assistant = assistant
        self.bot = None

    async def initialize(self):
        """Initialize Discord connection."""
        logger.info("Initializing Discord connector...")
        
        token = self.config.get('token')
        if not token:
            logger.error("Discord token not found in config")
            return
        
        # Create bot instance
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        
        @self.bot.event
        async def on_message(message: discord.Message):
            if message.author == self.bot.user:
                return
            
            if isinstance(message.channel, discord.DMChannel):
                response = await self.assistant.process_message(
                    message.content,
                    str(message.author.id)
                )
                await message.reply(f"🦞 {response}")
        
        logger.info("✓ Discord connector ready")

    async def start(self):
        """Start the Discord bot."""
        if self.bot:
            await self.bot.start(self.config.get('token'))
