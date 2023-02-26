import qrcode, shutil, os
from variables_module import dest, src
from PIL import Image

url = input("Enter link for QR Code: ")
logo = input("Enter logo for QR Code: ")
color = input("Enter color for QR Code: ")
name = input("Enter name for QR Code image: ")

logo = open(src, )

basewidth = 100

wpercent = (basewidth / (logo.size[0]))
hsize = int((float(logo.size[1] * float(wpercent))))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)

QRcode.add_data(url)
QRcode.make()
QRcolor = color

QRimage = QRcode.make_image(fill_color = QRcolor, back_color = "white").convert('RGB')

pos = ((QRimage.size[0] - logo.size[0]) // 2, (QRimage.size[1] - logo.size[1]) // 2)
QRimage.paste(logo, pos)

QRimage.save(name + '.png')
shutil.move(name + '.png', dest)

print("QR Code generated!")




