from DocumentCreator import DocumentCreator
from Document import Document
from WordDocument import WordDocument

class WordDocumentCreator(DocumentCreator):

    def factory_method(self) -> Document:
        return WordDocument()