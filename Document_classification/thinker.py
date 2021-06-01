from tkinter import *
import PyPDF2
from tkinter import filedialog
import classification
import yaml

if __name__ == '__main__':

    root = Tk()
    root.title('N1X10 - Classification PDF!')
    # root.iconbitmap('c:/gui/codemy.ico')
    root.geometry("500x500")

    # Create a textbox
    my_text = Text(root, height=30, width=60)
    my_text.pack(pady=10)

    # Clear the textbox
    def clear_text_box():
        my_text.delete(1.0, END)

    # Open our pdf file
    def open_pdf():
        # Grab the filename of the pdf file
        open_file = filedialog.askopenfilename(
            initialdir="C:/gui/",
            title="Open PDF File",
            filetypes=(
                ("PDF Files", "*.pdf"),
                ("All Files", "*.*")))

        # Check to see if there is a file
        if open_file:
            # Open the pdf file
            pdf_file = PyPDF2.PdfFileReader(open_file)
            # Set the page to read
            page = pdf_file.getPage(0)
            # Extract the text from the pdf file
            page_stuff = page.extractText()
            #class the page
            index = classification.DocumentClassification(open_file)
            # Add text to textbox
            # my_text.insert(1.0, index.pdf_mode)
            my_text.insert(2.0, yaml.dump(index.get_doc_index()))

            # my_text.insert(18.0, index.read_pdf)

    #Create A Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Add some dropdown menus
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_pdf)
    file_menu.add_command(label="Clear", command=clear_text_box)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)


    root.mainloop()