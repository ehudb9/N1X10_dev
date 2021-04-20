import numpy as np
import cv2
import pdf2image

from PIL import Image
import pytesseract

from pdf2image import convert_from_path

if __name__ == '__main__':
    pages = convert_from_path('C:\\Users\\feith\\Desktop\\N1X10\\20-4-21\\pdf_to_read.pdf', 300)    # pages is a list of images

    str = pytesseract.image_to_string(pages[0])
    hocr = pytesseract.image_to_pdf_or_hocr(pages[0], extension='hocr')   # Get HOCR output
    #xml = pytesseract.image_to_alto_xml(pages[0])     # Get ALTO XML output
    nate = pytesseract.image_to_alto_xml()
    print(type(str))
    print(type(hocr))

    print("hey Process-File-Type")