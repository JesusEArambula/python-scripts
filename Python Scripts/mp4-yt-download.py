from pytube import YouTube
from variables_module import *

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path = dest)
    except:
        print("An error has occurred")
    
    successMsg(youtubeObject.title)

link = input("Enter YouTube Video URL: ") 
Download(link)