import os
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog

import customtkinter
import shutil

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('400x300')
root.title('Rename Files')

def SelectPath():
    # Allows user to select the path from File Explorer/Finder
    path = filedialog.askdirectory()
    pathLabel.configure(text = path)

def Rename():

    os.chdir(pathLabel.cget('text'))

    count = 1

    for file in os.listdir():
        ext = os.path.splitext(file)[1]
        newName = nameField.get()

        newFile = '{}-{}{}'.format(newName, count, ext)
        print(newFile)

        os.rename(file, newFile)

        count += 1

# New file name label
nameLabel = customtkinter.CTkLabel(root, text = "Enter New File Name", font = ('Arial', 20))
nameLabel.pack(pady = 5, padx = 30)

# New file name input
nameField = customtkinter.CTkEntry(root, border_width = 0, placeholder_text = "New File Name", corner_radius = 10, width = 200, font = ('Arial', 16))
nameField.pack(pady = 20, padx = 30)

# Path field
pathLabel = customtkinter.CTkLabel(root, text = "Select folder to rename files", font = ('Arial', 20))
pathLabel.pack(pady = 5, padx = 30)

# Select Button for selecting path to download to
selectButton = customtkinter.CTkButton(root, width = 50, text = "Select", command = SelectPath, font = ('Arial', 16))
selectButton.pack(pady = 10, padx = 30)

# Download Button to start download
downloadButton = customtkinter.CTkButton(root, width = 80, height = 30, corner_radius = 30, text = "Rename", command = Rename, font = ('Arial', 16))
downloadButton.pack(pady = 10, padx = 30)

root.mainloop()