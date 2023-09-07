#!/usr/bin/env python3
"""
SessionAuth class module for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth class inherits from Auth class and implements the
    WWW Session Authentication scheme
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id