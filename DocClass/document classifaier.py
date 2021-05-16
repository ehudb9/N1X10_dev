import PyPDF2

# from DocClass.CONSTANS import * as con

__name__ = "document classifaier.py"
__author__ = "Ehud Barda"


class Pdf_Object:
    def __init__(self, file_link: str):
        self.pdfFileObj = open(file_link, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)
        # print(pdfReader.numPages)  # will give total number of pages in pdf
        # creating a page object
        pageObj = self.pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        self.pdfReader.close()


class Document_Classification:
    # can get "pdfObj" if the file is readable and "OCR" if its a scanner picture
    def __init__(self, file_path, mode="pdfObj"):
        self.doc_index = {
            "patient_name": "",
            "date_of_document": "",
            "date_of_procedure": "",
            "doctor_name": "",
            "department": "",
            "institution": "",
            "procedure_type": "",
            "num_of_pages": 0,
            "document_reference": ""
        }
        self.text = self.open_file(file_path)

    def search_line_index(self, word):
        """
        search for a given word in self.text
        return the line index where the word found. and -1 if wasn't found
        """
        pass

    def extract_type(self, text, index_key="procedure_type"):
        procedure_type = ""

        self.doc_index["procedure_type"] = procedure_type
        return procedure_type

    def open_file(self, path):
        # creating a pdf file object
        pdfFileObj = open(path, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()


# def imaging_type_line(filename, typ):
#     # open the sample text representing the imaging doc
#     doc = open(filename)
#
#     # read the content of the file opened
#     content = doc.readlines()
#
#     # pre-proccesing, could be in another function
#     fixed_content = [x.replace('\n', '') for x in content if x != '\n']
#
#     start_of_content = fixed_content[0:15]
#     index = 0
#     for line in start_of_content:
#         index += 1
#         # makes sure it's not part of another word
#         if typ+' ' in line or ' '+typ in line:
#             return index
#     return float('inf')
#
#
# def imaging_type(filename, imaging_types):
#     line_list = [float('inf')] * 5;
#     index = -1
#     for typ in imaging_types:
#         index += 1
#         line_list[index] = imaging_type_line(filename, typ)
#     return imaging_types[line_list.index(min(line_list))]


# main func for testing :

if __name__ == '__main__':
    # a = Pdf_Object(r'C:\Users\User\Desktop\N1X10\Sample documents\Dr summaries\AC 1.26.17 rad onc.pdf')
    print("ji")