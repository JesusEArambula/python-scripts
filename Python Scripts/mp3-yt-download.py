from pytube import YouTube
from variables_module import *
import os

yt = YouTube(str(input("Enter YouTube video URL: ")))
downloadingMsg()
video = yt.streams.filter(only_audio = True).first()

out_file = video.download(output_path = dest)
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"

os.rename(out_file, new_file)

successMsg(yt.title)
