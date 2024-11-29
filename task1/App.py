from abc import ABC, abstractmethod
from Document import Document
from WordDocumentCreator import WordDocumentCreator
from PDFDocumentCreator import PDFDocumentCreator
from ExcelDocumentCreator import ExcelDocumentCreator

class App(ABC):

    @abstractmethod
    def __init__(self):
        pass
    # Returns a new document object corrospoding to the App type. Prints creation message
    def new_document(self, type : str) -> Document:
        if type not in self.doc_types:
            print(f"{type} not supported in {self.__class__.__name__}")
            return None
        doc = self.doc_types[type].factory_method()
        print(doc.create())
        return doc



class BronzeApp(App):

    def __init__(self):
        self.doc_types = {"word": WordDocumentCreator}

class SilverApp(App):

    def __init__(self):
        self.doc_types = {"word": WordDocumentCreator, "pdf": PDFDocumentCreator}

class GoldApp(App):

    def __init__(self):
        self.doc_types = {"word": WordDocumentCreator, "pdf": PDFDocumentCreator, "excel": ExcelDocumentCreator}

