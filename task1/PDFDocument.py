from Document import Document

class PDFDocument(Document):

    def create(self) -> str:
        msg = "PDF document has been created"
        return msg