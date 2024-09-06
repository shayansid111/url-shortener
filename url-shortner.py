# Importing all the libraries
from tkinter import *  # Provides the tools to create a GUI.
import tkinter.messagebox as tkmsg  #Module in tkinter for creating message boxes.
import PIL   #Python Imaging Library, used for opening, manipulating, and displaying images in the GUI.
from PIL import ImageTk   
from PIL import Image
from tkinter import filedialog #A module to open file dialogs in the application.
import pyshorteners #Pyshorteners is a Python library that helps you shorten URLs using the most famous URL Shorteners available.
import clipboard #Used to interact with the clipboard for copying the shortened URL


# Function to short URL
#When the user inputs a URL and presses the "Shorten URL" button, the convert() function is triggered.
def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())

    Button(root, text="URL Shortened", bg="#F8C471", fg="#1e1e1e", font="poppins 11 bold", command=convert, relief=GROOVE).place(x=8, y=220)

    shorturl.set(s)
    clip = str(s)
    clipboard.copy(s)
    Label(root, text="Shortened URL is copied to clipboard; press Ctrl + V to paste", bg="#49f6b3", fg="#1e1e1e", font="poppins 9").place(x=8, y=360)

    
# Initialzing the tkinter root window
root = Tk()
root.title(" URL Shortner")
root.geometry("400x400")
root.resizable(False, False)
root.wm_iconbitmap("link.ico")
root.config(background="#4a536b")


image = Image.open('bg3.png')
test = ImageTk.PhotoImage(image)
label = Label(image=test, bg="#4a536b")
label.pack()


url = StringVar()
shorturl = StringVar()


Label(root, text="Enter URL Here ", bg="#2C3E50", fg="#EAECEE", font="poppins 13 bold", padx=3, pady=1).place(x=7, y=130)

Entry(root, textvariable=url, width=35, font="poppins 12").place(x=7, y=155)


Label(root, text="Shortened URL", bg="#2C3E50", fg="#fff", font="poppins 13 bold", padx=3, pady=1).place(x=8, y=300)

short = Entry(root, textvariable=shorturl, width=35,font="poppins 12")

short.place(x=8, y=325)



Button(root, text="Shorten URL", bg="#F8C471", fg="#1e1e1e", font="poppins 11 bold", command=convert, relief=GROOVE).place(x=8, y=220)

root.mainloop()#This keeps the GUI window open and responsive, waiting for user interaction.