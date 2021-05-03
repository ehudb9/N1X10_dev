# importing required modules
import PyPDF2
import tabula
import csv


def extract_words(file_name):
    pdf = PyPDF2.PdfFileReader(file_name)

    with open('ondexed.txt', 'w') as f:
        for page in range(pdf.numPages):
            print('page: {0}'.format(page))
            obj = pdf.getPage(page)
            try:
                txt = obj.extractText()
                print(''.center(100, '-'))
            except:
                pass
            else:
                f.write(txt)
        f.close()


def csv_reader(link):
    with open('address.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

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

def tabula(link):
    # readinf the PDF file that contain Table Data
    # you can find find the pdf file with complete code in below
    # read_pdf will save the pdf table into Pandas Dataframe
    df = tabula.read_pdf(link)
    # in order to print first 5 lines of Table
    df.head()

    #df2 = tabula.read_pdf(link, multiple_tables = True)

    #If you want the output into JSON Format
    #tabula.read_pdf("offense.pdf", output_format="json")

    #you can us Below code to convert the PDF Data into Excel or CSV
    tabula.convert_into("05_16_2019 Cytology-Non GYN.pdf", "05_16_2019 Cytology-Non GYN.pdf.xlsx", output_format="xlsx")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pypdf(r'C:\Users\ehudb\PycharmProjects\nixio test\05_16_2019 Cytology-Non GYN.pdf')
    #tabula('05_16_2019 Cytology-Non GYN.pdf')
