import PyPDF2

class Pdf_Object:
    def __init__(self, file_link:str):
        self.pdfFileObj = open(file_link, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)
        # print(pdfReader.numPages)  # will give total number of pages in pdf
        # creating a page object
        pageObj = self.pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        self.pdfReader.close()

class document_classification:
    def __init__(self, file , mode="pdfObj"):
        pass
    def search(word):
        """
        """
        pass

    def extract_word(word):
        """
        """
    def open_file(link):
        pass
