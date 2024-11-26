from DocumentCreator import DocumentCreator
from Document import Document
from WordDocument import WordDocument

class PDFDocumentCreator(DocumentCreator):

    def factory_method() -> Document:
        return WordDocument()