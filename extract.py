from PyPDF2 import PdfReader

# pdf file reader


reader = PdfReader("pdf_example.pdf")


page = reader.pages[0]


print(page.extract_text())