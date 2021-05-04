import PyPDF2
from DocClass.CONSTANS import *


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

class Document_Classification:
    def __init__(self, file , mode="pdfObj"):
        self.doc_index = {
            "patient_name" : "",
            "date_of_document" : "",
            "date_of_procedure" : "",
            "doctor_name" : "",
            "department": "",
            "institution": "",
            "procedure_type": "",
            "num_of_pages" : 0,
            "document_reference" : ""
        }
        self.text = file
    def search(word):
        """
        """
        pass

    def extract_type(self, text, index_key="procedure_type"):
        procedure_type = ""

        self.doc_index["procedure_type"] = procedure_type
        return procedure_type


    def open_file(link):
        pass

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
        print(procedure_types_EXP)