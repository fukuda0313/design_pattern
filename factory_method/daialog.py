from __future__ import annotations
from abc import ABC, abstractmethod
from button_interface import Button


class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        pass

    def render(self):
        button = self.create_button()
