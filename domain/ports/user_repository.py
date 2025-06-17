from abc import ABC, abstractmethod
from typing import Any


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, email: str, password: str) -> Any:
        """Persist user and return identifier."""
        raise NotImplementedError
