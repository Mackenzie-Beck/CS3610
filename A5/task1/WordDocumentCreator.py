from DocumentCreator import DocumentCreator
from Document import Document
from WordDocument import WordDocument

class WordDocumentCreator(DocumentCreator):

    @staticmethod
    def factory_method() -> Document:
        return WordDocument()