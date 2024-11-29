from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def create() -> str:
        pass