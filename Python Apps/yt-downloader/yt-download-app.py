from os import path
from moviepy import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import VideoFileClip

import customtkinter
import shutil

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry("500x400")
root.title("YouTube Downloader")
root.resizable(False, False)

def SelectPath():
    # Allows user to select the path from File Explorer/Finder
    path = filedialog.askdirectory()
    pathLabel.configure(text = path)

def DownloadFile():
    # Get user path
    getLink = linkField.get()
    # Get selected path
    userPath = pathLabel.cget("text")
    root.title('Downloading...')
    # Download Video
    mp4Video = YouTube(getLink).streams.get_highest_resolution().download()
    videoClip = VideoFileClip(mp4Video)
    videoClip.close()
    # Move file to selected directory
    shutil.move(mp4Video, userPath)
    root.title('YouTube Downloader')

# YouTube Logo Banner
YTImage = customtkinter.CTkImage(dark_image = Image.open("yt-logo.png"), size = (250, 100))
YTLabel = customtkinter.CTkLabel(root, text = "", image = YTImage)
YTLabel.pack(pady = 30, padx = 30)

# Link field
linkField = customtkinter.CTkEntry(root, border_width = 0, placeholder_text = "YouTube URL", width = 300, font = ('Arial', 13))
linkField.pack(pady = 20, padx = 30)

# Path field
pathLabel = customtkinter.CTkLabel(root, text = "Select path to download", font = ('Arial', 20))
pathLabel.pack(pady = 1, padx = 30)

# Select Button for selecting path to download to
selectButton = customtkinter.CTkButton(root, width = 50, text = "Select", command = SelectPath, font = ('Arial', 16))
selectButton.pack(pady = 10, padx = 30)

# Download Button to start download
downloadButton = customtkinter.CTkButton(root, width = 80, height = 30, corner_radius = 30, text = "Download", command = DownloadFile, font = ('Arial', 16))
downloadButton.pack(pady = 10, padx = 30)

root.mainloop()