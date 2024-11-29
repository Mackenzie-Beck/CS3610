from DocumentCreator import DocumentCreator
from Document import Document
from ExcelDocument import ExcelDocument

class ExcelDocumentCreator(DocumentCreator):

    @staticmethod
    def factory_method() -> Document:
        return ExcelDocument()