from DocumentCreator import DocumentCreator
from Document import Document
from PDFDocument import PDFDocument

class PDFDocumentCreator(DocumentCreator):

    def factory_method() -> Document:
        return PDFDocument()