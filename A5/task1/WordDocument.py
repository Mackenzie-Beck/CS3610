from Document import Document

class WordDocument(Document):

    def create(self) -> str:
        msg = "Word document has been created"
        return msg