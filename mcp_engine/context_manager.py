"""Manage user session contexts with persistence support."""

import logging
from typing import Dict, Optional
from threading import Lock

logger = logging.getLogger(__name__)

class ContextManager:
    """
    Thread-safe context manager for storing and retrieving per-user session data.
    """

    def __init__(self) -> None:
        self._contexts: Dict[str, Dict] = {}
        self._lock = Lock()

    def load_context(self, user_id: str) -> Dict:
        """
        Retrieve the current context for a user.

        Args:
            user_id: Unique user identifier.

        Returns:
            User context dictionary (empty if none exists).
        """
        with self._lock:
            context = self._contexts.get(user_id, {}).copy()
        logger.debug(f"Loaded context for user {user_id}: {context}")
        return context

    def update_context(self, user_id: str, new_data: Dict) -> None:
        """
        Update the stored context with new data.

        Args:
            user_id: Unique user identifier.
            new_data: Dictionary of new context data.
        """
        with self._lock:
            if user_id not in self._contexts:
                self._contexts[user_id] = {}
            self._contexts[user_id].update(new_data)
        logger.debug(f"Updated context for user {user_id} with {new_data}")

    def clear_context(self, user_id: str) -> None:
        """
        Clear context data for a user.

        Args:
            user_id: Unique user identifier.
        """
        with self._lock:
            if user_id in self._contexts:
                del self._contexts[user_id]
                logger.debug(f"Cleared context for user {user_id}")
            else:
                logger.debug(f"No context to clear for user {user_id}")
