from Clients import WordClient, PDFClient, ExcelClient

# Main uses the clients to create documents

word_client = WordClient()
pdf_client = PDFClient()
excel_client = ExcelClient()

word_doc = word_client.new_document()
pdf_doc = pdf_client.new_document()
excel_doc = excel_client.new_document()

