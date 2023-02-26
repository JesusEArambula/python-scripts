from PyPDF2 import PdfMerger
from variables_module import *
import shutil, os

fileList = [file for file in os.listdir(src) if file.endswith(".pdf")]

merger = PdfMerger()

pdfName = input("Enter name for the merged PDF file: ")
extensionName = pdfName + ".pdf"

for pdf in fileList:
    merger.append(open(src + pdf, "rb"))

with open(extensionName, "wb") as fout:
    merger.write(fout)

shutil.move(extensionName, dest)
