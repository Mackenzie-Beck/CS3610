from Document import Document

class ExcelDocument(Document):

    def create(self) -> str:
        msg = "Excel document has been created"
        return msg