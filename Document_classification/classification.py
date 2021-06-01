import pdfHandle
import PyPDF2
import re
import yaml
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from datetime import datetime

procedure_types_EXP = {
    'Pathology and Surgery': ["Pathology", "CYTOPATHOLOGY", "Surgical Procedure", "SURGICAL", "Surgical", "PATHOLOGY"],
    "Medication prescriptions": ["Medication", "Medications"],
    "Imaging": ["CT", "XR", "NM", "FDG", "PET/CT", "PET", 'XR', 'MRI', 'PET CT', 'CT', 'DOTATATE'],
    "Blood Test": ["Collection Information", "METABOLIC", "LAB RESULT"],
    "Dr summaries": [""],
    "Hospital release forms": [""],
    "Medication prescriptions": [""],
}
TITLES = ["report", "summery", "result"]
DOC_DATE = ["date of report"]
date_of_procedure = ["Collection", "collected", "s" ]
institution_list = [""]


class DocumentClassification:
    """

    gets path to file and output set of index that describe and verify the file.
    procedure check that the file belongs to the patient,
    return the document relevant date (event date) and
    return document type out of a list of types (stored in file_type_list)

    :param str: path to file
    :param (optional)str: patient full name
    """

    def __init__(self, file_path, patient_name=None):
        page_num = 0
        self.patient_name = patient_name
        self.pdf_mode = "pdfObj"
        with open(file_path, "rb") as self.f:
            reader = PyPDF2.PdfFileReader(self.f)
            page = reader.getPage(0)
            page_num = reader.getNumPages()
            self.read_pdf = page.extractText()

        if len(self.read_pdf) < 10:
            self.read_pdf = self.convert_pdf_to_txt(file_path)
            self.pdf_mode = "hackPdf"
            if len(self.read_pdf) < 10 or self.read_pdf[0] == "(":
                # ocr
                print("---------____needed to acrivate OCR mode____---------\n\n\n\n")
                self.pdf_mode = "OCR"
                # TBC on colab
                self.read_pdf = self.ocr_pdf_to_str(file_path)
        # remove empty lines
        self.remove_empty_lines()

        self.doc_index = {
            "patient_name": self.get_patient_name(),
            "date_of_document": self.get_doc_date(),
            "date_of_procedure": self.get_procedure_date(),
            "doctor_name": self.get_doctor_name(),
            # "department": self.get_department(),
            "institution": self.get_get_institution_name(),
            "procedure_type": self.extract_type(),
            "num_of_pages": page_num,
            "document_reference": file_path
        }

    def close_file(self):
        """

        close the file obj
        """
        self.f.close()

    def get_doc_index(self):
        """

        :return: dict: the given doc_index
        """
        return self.doc_index
        # to print use:
        # import yaml
        # print(yaml.dump(a.get_doc_index()))

    def remove_empty_lines(self):
        """
        rempves empty line in the text
        """
        lines = self.read_pdf.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        string_without_empty_lines = ""
        for line in non_empty_lines:
            string_without_empty_lines += line + "\n"

        self.read_pdf = string_without_empty_lines

    def _print_index(self):
        """

        prints the doc_index(JSON/DICT)
        """
        print(yaml.dump(self.get_doc_index()))

    def get_text(self) -> str:
        """

        :return: str: doc text - in lower case
        """
        return self.read_pdf.lower()

    def get_doctor_name(self):
        """

        :return: str doctor name
        """
        lines = "\n".join(self.read_pdf.splitlines()[2:20])
        pattern = re.compile(r'([A-Z]\w+[^:\n]+)\s(MD|M\.D\.)')
        search = re.search(pattern, lines)
        if search:
            return search.group()

    def get_get_institution_name(self):
        """

        :return: str :  institution_name
        """
        # problem with read from pictures
        pass

    def get_doc_date(self):
        pass

    def get_procedure_date(self):
        pass

    def convert_pdf_to_txt(self, path) -> str:
        """
        read pdf file and conevt the text to str using pdfminer
        :param path: file input
        :return: str: file's text in str
        """
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                      check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        return text

    def ocr_pdf_to_str(self, path):
        """
        MUST CONNECT TO OCR MODULE
        :return: str : file text
        """
        str_lst = ["CONNECT", "OCR", "!"]
        # img_lst = convert_pdf_to_image_list(path)
        # str_lst = convert_list_of_images_to_list_of_str(img_lst)
        txt = '\n'.join([i for i in str_lst[1:]])
        return txt

    def extract_type(self):
        """
        Go through the first 15 lines and get the type
        from a constant list of types

        :return: str : document type
        """
        lines = self.get_text().splitlines()
        num_line = 2
        types = {}
        for line in lines[2:15]:
            for type in procedure_types_EXP:
                for term in procedure_types_EXP[type]:
                    words = line.split()
                    for word in words:
                        if word == term.lower():
                            types[num_line] = type

            num_line += 1
        if len(types) == 0:
            return None
        return (min(types.items(), key=lambda x: x[0])[1])

    def search_line_index(self, word):
        """
        search for a given word in self.text
        return the line index where the word found. and -1 if wasn't found
        """
        pass

    def get_patient_name(self):
        """
        Check if a given patient name is correct
        and set the name if was't given a name
        """
        if self.patient_name is None:
            match = re.search(r'(patient|name|patient name): (\w+\s\w+)', self.read_pdf.lower())
            if match:
                return match.group(2)
            else:
                return "no name"
        name = self.patient_name.split()
        i = 0
        lines = self.get_text().splitlines()
        for line in lines[2:15]:
            list_line = line.split()
            for a in name:
                if a in list_line:
                    i +=1
            if i == len(name):
                return self.patient_name
            i = 0
        return "no name"


    #   for colab- calling ocr methods
    # def ocr_convert_pdf_to_str(self, path):
    #     img_lst = self.convert_pdf_to_image_list(path)
    #     str_lst = self.convert_list_of_images_to_list_of_str(img_lst)
    #     txt = '\n'.join([i for i in str_lst[1:]])
    #     return txt


# main func for testing :
if __name__ == '__main__':
    # a = DocumentClassification(r"C:\Users\ehudb\PycharmProjects\nixio test\Sample documents\Pathology\2019.6.26. endobronchial bx.pdf")
    a = DocumentClassification(
        r"C:\Users\ehudb\PycharmProjects\nixio test\Sample documents\Pathology\2016.4.14. Brigham slide review.pdf")
    a = DocumentClassification(r"C:\Users\ehudb\PycharmProjects\nixio test\Sample documents\Pathology\2016.4.14. Brigham slide review.pdf")
    # # print(a.print_indexs)
    print(yaml.dump(a.get_doc_index()))
    # a.close_file()

    # a = DocumentClassification(
    #     r"C:\Users\ehudb\PycharmProjects\nixio test\Sample documents\Pathology\2016.4.15 pleural and LN bx.pdf")
    # #print(a._print_index())
    # # print(yaml.dump(a.get_doc_index()))
    # print(a.read_pdf)
    # print(a.pdf_mode)
    # a.close_file()

    # initializing string
    # test_str = "gfg at 2021-01-04"
    #
    # # printing original string
    # print("The original string is : " + str(test_str))
    #
    # # searching string
    # match_str = re.search(r'\d{4}-\d{2}-\d{2}', test_str)
    #
    # # computed date
    # # feeding format
    # res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()
    # # printing result
    # print("Computed date : " + str(res))
    #
    # txt = "sdnckjlsndm"
    # pattern = re.compile(r'[a-zA-Z]')
    # matches = pattern.finditer(txt)
    # for match in matches:
    #     print(match)