from abc import ABC, abstractmethod
from typing import Any


class Presenter(ABC):
    @abstractmethod
    def present(self, data: Any) -> Any:
        """Format the use case result."""
        raise NotImplementedError
