import pytube
import tkinter
from tkinter import * 
from pytube import YouTube


def download_video():
    url = url_entry.get()
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        status_label.config(text= "Download Successful!", fg ="green" )    
    except Exception as e:
        status_label.config (text = "Error: " + str(e) + " Please check the URL.", fg = "red" )

root=Tk()
root.title("Youtube Video Downloader")
root.geometry("500x600")

url_label = Label(root, text = "Enter YouTube Video URL :")
url_label.pack(pady=10)

url_entry = Entry(root, width =50)
url_entry.pack(pady=10)

download_button= Button(root, text = "Download Video", command = download_video)
download_button.pack(pady=10)

status_label = Label(root, text="")
status_label.pack()

root.mainloop()
