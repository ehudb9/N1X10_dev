# Tesseract dependencies
# !pip install pytesseract
# !sudo apt install tesseract-ocr
# Poppler  dependencies
# !apt-get install poppler-utils
# !pip install pdf2image

# will work in locall or VM colab
from pdf2image import convert_from_path
import pytesseract
poppler_path=r'C:\\Users\\ehudb\\Desktop\\OS\\poppler-0.68.0\\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

class ocr_convert:
    def __init__(self, path):
        self.path = path
        self.txt = self.convert_pdf_to_image_list()

    def convert_pdf_to_image_list(self):
        """
            this function converts pdf to a python list of <class 'PIL.PpmImagePlugin.PpmImageFile'> images.
            Parameters
            ----------
            pdf_path : string
                pdf_path is the local path of the pdf file on given machine.
            Returns
            -------
            list
                Python list of <class 'PIL.PpmImagePlugin.PpmImageFile'> images,
                where each image corresponds to a single pdf page.
            """
        pages = convert_from_path(self.path, 300)  # pages is a list of images
        return pages

    def convert_list_of_images_to_list_of_xml(self, img_lst):
        """
            this function converts a list of images to a list of xml (type=byte).
            Parameters
            ----------
            img_lst : Python list of <class 'PIL.PpmImagePlugin.PpmImageFile'> images.
            Returns
            -------
            Python list
                Python list of xml(type=byte) corresponding to img_lst.
            """
        lst_of_xml = []
        for img in img_lst:
            lst_of_xml.append(pytesseract.image_to_pdf_or_hocr(img, extension='hocr'))  # Get HOCR output)
        return lst_of_xml

    def convert_list_of_images_to_list_of_str(self, img_lst):
        """
            this function converts a list of images to a list of strings.
            Parameters
            ----------
            img_lst : Python list of <class 'PIL.PpmImagePlugin.PpmImageFile'> images.
            Returns
            -------
            Python list
                Python list of strings corresponding to img_lst.
            """
        lst_of_str = []
        for img in img_lst:
            lst_of_str.append(pytesseract.image_to_string(img))
        return lst_of_str

    def convert_pdf_to_str(self):
        # file_path = "C:\\Users\\feith\\Desktop\\simple-test-pdf.pdf"

        img_lst = self.convert_pdf_to_image_list()
        str_lst = self.convert_list_of_images_to_list_of_str(img_lst)
        txt = '\n'.join([i for i in str_lst[1:]])
        return txt


#  main method for test:
if __name__ == '__main__':
    a = ocr_convert("a.pdf")
    print(a.txt)
