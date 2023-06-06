import logging
from typing import Optional

import strawberry

from .base import BaseType

logger = logging.getLogger(__name__)

@strawberry.type
class UserType(BaseType):
    id: int
    username: str


@strawberry.input
class UserInput:
    username: str


@strawberry.input
class UserUpdate:
    username: Optional[str] = None