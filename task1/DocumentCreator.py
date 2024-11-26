from abc import ABC, abstractmethod
from Document import Document

class DocumentCreator(ABC):

    @abstractmethod
    def factory_method() -> Document:
        pass
    
    def create_document(self) -> str:
        doc = self.factory_method()
        return doc.create()