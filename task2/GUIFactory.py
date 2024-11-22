from abc import ABC, abstractmethod

class GUIFactory(ABC):

    @abstractmethod
    def createButton(self) -> 'Button':
        pass

    @abstractmethod
    def createCheckbox(self) -> 'Checkbox':
        pass