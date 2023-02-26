from os import path
from moviepy import *
from tkinter import *
from moviepy.editor import VideoFileClip
from tkinter import filedialog
from pytube import YouTube

import shutil
import customtkinter

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('green')

# Functions
def SelectPath():
    # Allows user to select the path from File Explorer/Finder
    path = filedialog.askdirectory()
    pathLabel.configure(text = path)

def DownloadFile():
    # Get user path
    getLink = linkField.get()
    # Get selected path
    userPath = pathLabel.cget("text")
    screen.title('Downloading...')
    # Download Video
    mp4Video = YouTube(getLink).streams.get_highest_resolution().download()
    videoClip = VideoFileClip(mp4Video)
    videoClip.close()
    # Move file to selected directory
    shutil.move(mp4Video, userPath)
    screen.title('YouTube Downloader')


screen = customtkinter.CTk()
screen.geometry("500x500")

# Logo image sizing
logoImage = PhotoImage(file = 'yt-logo.png')
logoImage = logoImage.subsample(4, 4)



# URL field
linkField = customtkinter.CTkEntry(screen, width = 500)
linkLabel = customtkinter.CTkLabel(screen, text = "Enter YouTube URL", font = ('Arial', 15))

# Select path for file destination
pathLabel = customtkinter.CTkLabel(screen, text = "Select path for download", font = ('Arial', 15))
selectButton = customtkinter.CTkButton(screen, text = "Select", command = SelectPath)

# Add to window
linkField.pack(pady = 20, padx = 60)
linkLabel.pack(pady = 20, padx = 60)

# Add Widgets to Window
pathLabel.pack(pady = 20, padx = 60)
selectButton.pack(pady = 20, padx = 60)

# Download button
downloadButton = customtkinter.CTkButton(screen, text = "Download", command = DownloadFile)
# Add download button to canvas
downloadButton.pack(pady = 20, padx = 60)


screen.mainloop()
