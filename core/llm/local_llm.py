"""Local LLM engine using Ollama or Llama.cpp."""

from typing import Dict, Optional, List
from loguru import logger


class LocalLLM:
    """Local Language Model wrapper."""

    def __init__(self, config: Dict):
        self.config = config
        self.model = None
        self.client = None

    async def initialize(self):
        """Initialize the local LLM."""
        logger.info("Initializing local LLM...")
        
        try:
            # Try to use Ollama first
            import ollama
            self.client = ollama
            logger.info("✓ Using Ollama for local LLM")
        except ImportError:
            logger.warning("Ollama not available, trying llama-cpp-python...")
            try:
                from llama_cpp import Llama
                self.client = Llama
                logger.info("✓ Using llama-cpp-python for local LLM")
            except ImportError:
                raise RuntimeError("No local LLM engine available. Install ollama or llama-cpp-python.")

    async def generate(self, message: str, context: List[str], personality: Dict) -> str:
        """Generate a response using the local LLM.
        
        Args:
            message: User message
            context: Previous conversation context
            personality: Personality configuration
            
        Returns:
            Generated response
        """
        # Build system prompt with personality
        system_prompt = self._build_system_prompt(personality)
        
        # Build context
        full_context = "\n".join(context[-5:]) if context else ""
        
        # Placeholder for actual LLM call
        # In real implementation, this would call the actual model
        response = f"🦞 I'm still learning! In the meantime, here's what I understood: '{message}'"
        
        return response

    def _build_system_prompt(self, personality: Dict) -> str:
        """Build system prompt from personality config."""
        name = personality.get('name', 'Lobster')
        tone = personality.get('tone', 'friendly')
        theme = personality.get('theme', 'quirky')
        
        prompt = f"""
You are {name}, a personal AI assistant with a {tone} tone and {theme} personality.
You are helpful, harmless, and honest. You run locally on the user's device, so privacy is paramount.
You care about the user's data staying private and never leaving their device.
Your responses should be concise and practical, with a touch of {theme} charm.
"""
        
        return prompt.strip()

    async def cleanup(self):
        """Cleanup LLM resources."""
        pass
