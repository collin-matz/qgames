"""Interface for Game types."""

from abc import ABC, abstractmethod


class Game(ABC):
    @abstractmethod
    def render(self) -> str:
        ...

    @abstractmethod
    def next_turn(self):
        ...