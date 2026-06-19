"""Core AI Assistant Engine."""

import asyncio
from typing import Optional, List, Dict
from loguru import logger


class LobsterAssistant:
    """Main AI Assistant class."""

    def __init__(self, config: Dict):
        self.config = config
        self.llm = None
        self.memory = None
        self.personality = config.get('personality', {})

    async def initialize(self):
        """Initialize the AI engine."""
        logger.info("Initializing AI engine...")
        
        # Initialize LLM
        from core.llm import LocalLLM
        self.llm = LocalLLM(self.config.get('ai', {}))
        await self.llm.initialize()
        
        # Initialize memory
        from core.memory import Memory
        self.memory = Memory()
        
        logger.info("✓ AI engine ready")

    async def process_message(self, message: str, user_id: str) -> str:
        """Process a user message and return a response.
        
        Args:
            message: The user's input message
            user_id: Unique identifier for the user
            
        Returns:
            The assistant's response
        """
        logger.info(f"Processing message from {user_id}: {message[:50]}...")
        
        try:
            # Get conversation context
            context = await self.memory.get_context(user_id)
            
            # Generate response
            response = await self.llm.generate(
                message=message,
                context=context,
                personality=self.personality
            )
            
            # Store in memory
            await self.memory.store_exchange(user_id, message, response)
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return "🦞 Oops! Something went wrong. Let me catch my breath and try again!"

    async def cleanup(self):
        """Cleanup resources."""
        if self.llm:
            await self.llm.cleanup()
        if self.memory:
            await self.memory.cleanup()
