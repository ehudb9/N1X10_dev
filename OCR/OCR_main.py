from pdf2image import convert_from_path
import pytesseract


def convert_pdf_to_image_list(pdf_path):
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
    pages = convert_from_path(pdf_path, 300)  # pages is a list of images
    return pages


def convert_list_of_images_to_list_of_str(img_lst):
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


def convert_list_of_images_to_list_of_xml(img_lst):
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
