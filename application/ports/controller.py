from abc import ABC, abstractmethod
from typing import Any


class Controller(ABC):
    @abstractmethod
    def handle(self, data: Any) -> Any:
        """Handle request data."""
        raise NotImplementedError
