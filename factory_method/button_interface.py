from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self, function):
        pass


class window_button(Button):

    def render():
        pass

    def onClick():
        pass


class html_button(Button):

    def render():
        pass

    def onClick():
        pass
