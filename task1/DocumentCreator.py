from abc import ABC, abstractmethod

class DocumentCreator(ABC):

    @abstractmethod
    def factory_method() -> Document:
        pass
    
    @abstractmethod
    def create_document() -> str:
        pass