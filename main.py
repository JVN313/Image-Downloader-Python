import requests
from tkinter import *

i = 0

def image_getter(url):
     r = requests.get(url)
     image_open= open(f"image{i}.png", "wb")
     image_open.write(r.content)
     image_open.close()

def Download_Value():
    global i
    i += 1
    url = entry.get()
    image_getter(url)

window =Tk()

entry = Entry(window)

entry.pack(side=LEFT)

download_button = Button(window,text="Download",command=Download_Value)
download_button.pack(side=RIGHT)

window.mainloop()

image_getter(Download_Value())
