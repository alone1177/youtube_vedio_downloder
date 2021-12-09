# pip install requests
# pip install pytube

# This is the youtube vedio downloder

import requests as r
from pytube import YouTube

link = input("\033[01;33;40mEnter the link : \033[01;36;40m")
yt = YouTube(link)

# request
x = r.get(link)
if x.status_code == 200:
	print(f"\033[01;33;40mstatus : \033[01;32;40m{x.status_code} \033[00;00;40m")
else:
	print(f"\033[01;33;40mstatus : \033[01;31;40m{x.status_code} \033[00;00;40m")

# title

title = yt.streams[0].title
print(f"\033[01;33;40mTitle : \033[01;36;40m{title} \033[00;00;40m")

# description
des = yt.description
if des == "":
	print("\033[01;33;40mDescripiton : \033[01;35;40mNone\033[00;00;40m")
else:
	print(f"\033[01;33;40mDescripiton : \033[01;36;40m{des} \033[00;00;40m")

# vedio

print("       	\033[01;33;40m1) \033[01;32;40m240 \033[01;37;40m|| \033[01;33;40m2) \033[01;32;40m360 \033[01;37;40m|| \033[01;33;40m3) \033[01;32;40m720\033[01;37;40m|| \033[01;33;40m4) \033[01;32;40m1080")

res = int(input("\033[01;33;40mOption : \033[01;36;40m"))

if res == 1:
	down = yt.streams.filter(resolution="240p", file_extension="mp4").first()

elif res == 2:
	down = yt.streams.filter(resolution="36p", file_extension="mp4").first()

elif res == 3:
	down = yt.streams.filter(resolution="720p", file_extension="mp4").first()

elif res == 4:
	down = yt.streams.filter(resolution="1080p", file_extension="mp4").first()

# audio

#down = yt.streams.get_audio_only()

# Download

print("\033[01;35;40mDownload started !")

down.download("Youtube_vedio/")

print("\033[01;32;40mDownloaded ! \033[00;00;40m")
