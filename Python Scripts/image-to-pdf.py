import img2pdf
from PIL import Image
import os

imagePath = input("Enter image name: ")

pdfPath = input("Enter PDF name: ")

openImage = Image.open(imagePath)

pdfBytes = img2pdf.convert(openImage.filename)

file = open(pdfPath, "wb")

file.write(pdfBytes)

openImage.close()

print("Successfully made PDF file!")