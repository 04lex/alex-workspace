from PyPDF2 import PdfFileReader, PdfFileWriter

def get_pages_count(path):
    pdf = PdfFileReader(path)
    return pdf.getNumPages()

def cut_pdf(path, start_page, stop_page, outputpath="outputfile.pdf"):
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    for i in range(start_page - 1, stop_page):
        page = pdf.getPage(i)
        pdf_writer.addPage(page)

    with open(outputpath, "wb") as f:
        pdf_writer.write(f)


if __name__ == "__main__":
    path = "testfile.pdf"
    cut_pdf(path, 4, 7, "hello.pdf")