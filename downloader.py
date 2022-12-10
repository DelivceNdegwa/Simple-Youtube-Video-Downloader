from pytube import YouTube
from sys import argv
import os
from pathlib import Path

input_link = str(argv[1])

yt_object = YouTube(input_link)

print(f"Video title: {yt_object.title}")
print(f"Number of views: {yt_object.views}")

downloader = yt_object.streams.get_highest_resolution()

download_path = os.path.join(Path.home(), "Downloads/YT_Downloaded_Videos")

if not os.path.exists(download_path):
    os.makedirs(download_path)

print("Downloading ...")
downloader.download(download_path)
print(f"Video downloaded at {download_path}")

