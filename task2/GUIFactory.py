from abc import ABC, abstractmethod
from button import Button
from checkbox import Checkbox

class GUIFactory(ABC):

    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass