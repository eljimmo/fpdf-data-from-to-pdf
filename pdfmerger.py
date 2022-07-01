from PyPDF2 import PdfMerger

merger = PdfMerger()


for pdf in ["***.pdf", "****.pdf", "***.pdf"]:
    merger.append(pdf)

merger.write("***-pdf.pdf")
merger.close()

