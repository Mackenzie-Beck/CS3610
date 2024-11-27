from abc import ABC, abstractmethod
from Document import Document
from WordDocumentCreator import WordDocumentCreator
from PDFDocumentCreator import PDFDocumentCreator
from ExcelDocumentCreator import ExcelDocumentCreator

class Client(ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    # Returns a new document object corrospoding to the client type. Prints creation message
    def new_document(self) -> Document:
        doc = self.creator.factory_method()
        print(doc.create())
        return doc


class WordClient(Client):

    def __init__(self):
        self.creator = WordDocumentCreator()


class PDFClient(Client):

    def __init__(self):
        self.creator = ExcelDocumentCreator()


class ExcelClient(Client):

    def __init__(self):
        self.creator = PDFDocumentCreator()