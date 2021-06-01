# importing required modules
import PyPDF2
# import tabula
# import csv
# # import matplotlib
# # matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
#
# from py_pdf_parser.loaders import load_file
# # from py_pdf_parser.visualise import visualise
# from py_pdf_parser.loaders import load_file
# from py_pdf_parser.loaders import load_file
# from py_pdf_parser.visualise import visualise
# #
# # document = load_file("order_summary.pdf")
# # visualise(document)
# # def parser(path):
# #
# #     # Step 1 - Load the document
# #     document = load_file(path)
# #
# #     # We could visualise it here to check it looks correct:
# #     # from py_pdf_parser.visualise import visualise
# #     #visualise(document)
# #
# #     # Step 2 - Extract reference elements:
# #     to_element = document.elements.filter_by_text_equal("Patient Name::").extract_single_element()
# #     from_element = document.elements.filter_by_text_equal("FROM:").extract_single_element()
# #     date_element = document.elements.filter_by_text_equal("DATE:").extract_single_element()
# #     subject_element = document.elements.filter_by_text_equal("SUBJECT:").extract_single_element()
# #
# #     # Step 3 - Extract the data
# #     to_text = document.elements.to_the_right_of(to_element).extract_single_element().text()
# #     from_text = (
# #         document.elements.to_the_right_of(from_element).extract_single_element().text()
# #     )
# #     date_text = (
# #         document.elements.to_the_right_of(date_element).extract_single_element().text()
# #     )
# #     subject_text_element = document.elements.to_the_right_of(
# #         subject_element
# #     ).extract_single_element()
# #     subject_text = subject_text_element.text()
# #
# #     content_elements = document.elements.after(subject_element)
# #     content_text = "\n".join(element.text() for element in content_elements)
# #
# #     output = {
# #         "Patient Name": to_text,
# #         "from": from_text,
# #         "date": date_text,
# #         "subject": subject_text,
# #         "content": content_text,
# #     }
# #     print(output)
#
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr,  laparams=laparams)
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

# def extract_words_to_txt_file(pdf):
#
#
#     with open('ondexed.txt', 'w') as f:
#         for page in range(pdf.numPages):
#             print('page: {0}'.format(page))
#             obj = pdf.getPage(page)
#             try:
#                 txt = obj.extractText()
#                 print(''.center(100, '-'))
#             except:
#                 pass
#             else:
#                 f.write(txt)
#         f.close()
#
#
# def csv_reader(link):
#     with open('address.csv', 'r') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             print(row)

def pypdf(urlLink):
    # creating a pdf file object
    pdfFileObj = open(urlLink, 'rb')

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

# def tabula(link):
#     # readinf the PDF file that contain Table Data
#     # you can find find the pdf file with complete code in below
#     # read_pdf will save the pdf table into Pandas Dataframe
#     df = tabula.read_pdf(link)
#     # in order to print first 5 lines of Table
#     df.head()
#
#     #df2 = tabula.read_pdf(link, multiple_tables = True)
#
#     #If you want the output into JSON Format
#     #tabula.read_pdf("offense.pdf", output_format="json")
#
#     #you can us Below code to convert the PDF Data into Excel or CSV
#     tabula.convert_into("05_16_2019 Cytology-Non GYN.pdf", "05_16_2019 Cytology-Non GYN.pdf.xlsx", output_format="xlsx")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pypdf(r"C:\Users\ehudb\PycharmProjects\nixio test\Sample documents\Pathology\2016.4.14. Brigham slide review.pdf")
    #tabula('05_16_2019 Cytology-Non GYN.pdf')
    # for line in convert_pdf_to_txt('a.pdf').splitlines():
    #     print(line)
    #parser("a.pdf")
    #
    #
    # document = load_file("a.pdf")
    # print([element.text() for element in document.elements])
    # print(convert_pdf_to_txt(r"C:\Users\ehudb\PycharmProjects\nixio test\Sample documents\Pathology\2016.4.14. Brigham slide review.pdf"))



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

