from DocumentCreator import DocumentCreator
from Document import Document
from ExcelDocument import ExcelDocument

class ExcelDocumentCreator(DocumentCreator):

    def factory_method(self) -> Document:
        return ExcelDocument()