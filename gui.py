from tkinter import *
from tkinter import filedialog
import PyPDF2

root = Tk()
root.title("hello world")
root.iconbitmap()
root.geometry("500x500")

#text box dimensions

my_text = Text(root, height=30, width=60)
my_text.pack(pady=10)

# option:: clear text box
def Clear_text_box():
    my_text.delete(1.0, END)

# option::open pdf file, then grab file name,
def open_pdf():

    open_file =filedialog.askopenfilename(
        initialdir="C:/Users/***/",
        title="Open PDF File",
        filetypes=(
            ("PDF Files", "*pdf"),
            ("All Files", "*.*")))

            #check for file
    if open_file:
                pdf_file = PyPDF2.PdfFileReader(open_file)
                page = pdf_file.getPage(0)
                # extract text from pdf
                page_text = page.extractText()

                my_text.insert(1.0, page_text)




my_menu = Menu(root)
root.config(menu=my_menu)


# dropdown menus

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=Clear_text_box)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)




root.mainloop()