import PyPDF2
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
from io import StringIO
from DocClass.CONSTANS import *

# __name__ = "document_classifaier.py"
# __author__ = "Ehud Barda"


# class Pdf_Object:
#     def __init__(self, file_link: str):
#         self.pdfFileObj = open(file_link, 'rb')
#         self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)
#         # print(pdfReader.numPages)  # will give total number of pages in pdf
#         # creating a page object
#         pageObj = self.pdfReader.getPage(0)

#         # extracting text from page
#         print(pageObj.extractText())

#         # closing the pdf file object
#         self.pdfReader.close()


class Document_Classification:
    # can get "pdfObj" if the file is readable and "OCR" if its a scanner picture
    def __init__(self, file_path, mode="pdfObj"):
        
        # self.text = self.open_file(file_path)
        self.read_pdf = PyPDF2.PdfFileReader(file_path)
        
        self.doc_index = {
            "patient_name": self.get_patient_name(),
            "date_of_document": self.get_doc_date(),
            "date_of_procedure": self.get_procedure_date(),
            "doctor_name": self.get_doctor_name(),
            # "department": self.get_department(),
            "institution": self.get_get_institution_name(),
            "procedure_type": self.extract_type(),
            "num_of_pages": 0,
            "document_reference": file_path
        }
        
    def get_doc_index(self):
        return self.doc_index


    def get_doctor_name(self):
        pass
    
    def get_get_institution_name(self):
        pass
    
    def get_doc_date(self):
        pass
    
    def get_procedure_date(self):
        pass
    
    
    def extract_type(self, index_key="procedure_type"):
        procedure_type = ""
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        for type in procedure_types_EXP.keys():
            for line in page:
            words = page.split()
            for word in words:
                if word in procedure_types_EXP[type]:
                    pass
        self.doc_index["procedure_type"] = procedure_type
        return procedure_type

    def search_line_index(self, word):
        """
        search for a given word in self.text
        return the line index where the word found. and -1 if wasn't found
        """
        pass
    
    def get_patient_name(self):
        pass
    
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


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text
if __name__ == '__main__':
    # main()
    print("HI")
    # a = Pdf_Object(r'C:\Users\User\Desktop\N1X10\Sample documents\Dr summaries\AC 1.26.17 rad onc.pdf')
    print("ji")
    # with open('ondexed.txt', 'w') as f:
    #     f.write("hiii")
    # pdfFileObj = open(r'C:\Users\User\Desktop\N1X10\Sample documents\Dr summaries\AC 1.26.17 rad onc.pdf', 'rb')
    # read_pdf = PyPDF2.PdfFileReader(pdfFileObj)
    # page = read_pdf.getPage(0)
    # page_content = page.extractText()
    # print(page_content)