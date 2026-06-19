"""Local memory and conversation context storage."""

import sqlite3
from datetime import datetime
from typing import List, Dict
from pathlib import Path
from loguru import logger


class Memory:
    """Local conversation memory."""

    def __init__(self, db_path: str = "memory.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize SQLite database for memory."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY,
                    user_id TEXT,
                    message TEXT,
                    response TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    async def get_context(self, user_id: str, limit: int = 10) -> List[str]:
        """Get recent conversation context for a user."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT message, response FROM conversations
                WHERE user_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
            """, (user_id, limit))
            
            rows = cursor.fetchall()
            context = []
            for msg, resp in reversed(rows):
                context.append(f"User: {msg}")
                context.append(f"Assistant: {resp}")
            
            return context

    async def store_exchange(self, user_id: str, message: str, response: str):
        """Store a user message and assistant response."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO conversations (user_id, message, response)
                VALUES (?, ?, ?)
            """, (user_id, message, response))
            conn.commit()

    async def cleanup(self):
        """Cleanup memory resources."""
        pass
