import requests
import datetime 
from tkinter import *

i = 0
x = datetime.datetime.now()
time = x.strftime("%m%d%y%I%M%S")

def image_getter(url):
     r = requests.get(url)
     image_open= open(f"image{str(i)+time}.png", "wb")
     image_open.write(r.content)
     image_open.close()

def Download_Value():
    global i
    i += 1
    url = entry.get()
    image_getter(url)

window =Tk()
window.title("Image Getter")
window.geometry("250x65")
icon = PhotoImage(file="assets/icon.png")
window.iconphoto(True,icon)

label = Label(window, text="Type Image Url or Use CTRL + V To Paste Url")
label.pack()

entry = Entry(window)
entry.pack(side=LEFT)

download_button = Button(window,text="Download",command=Download_Value)
download_button.pack(side=RIGHT)

window.mainloop()