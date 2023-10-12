import ssl
import pytube
from pytube import YouTube


ssl._create_default_https_context = ssl._create_stdlib_context
link = input("Please, Enter Your Youtube Video URL:")
link = str(link)
youtube = pytube.YouTube(link)
youtube.streams.first().download()

print("Video Has Been Downloaded", link)