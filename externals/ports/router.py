from abc import ABC, abstractmethod
from fastapi import APIRouter


class Router(ABC):
    @property
    @abstractmethod
    def router(self) -> APIRouter:
        """Return configured APIRouter."""
        raise NotImplementedError
