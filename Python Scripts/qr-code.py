import pyqrcode, png, shutil
from variables_module import *
from pyqrcode import QRCode

link = input("Enter website link: ")
qrCodeName = input("Enter name for QR Code: ")

url = pyqrcode.create(link)

url.png(qrCodeName + ".png", scale = 6)

shutil.move(qrCodeName + ".png", dest)