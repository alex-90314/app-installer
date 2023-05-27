from tkinter import *
from tkinter import ttk
import os

root = Tk()
os.system("cls")
#sets the button click to run code
def butt_click():
    os.system("cls")
    os.system('python C:\\Users\\boric\\Documents\\GitHub\\app-installer\\backend.py')

#setting up the frame
frm = ttk.Frame(root, padding=10)
frm.grid()

#setting up start & stop buttons
hello_label = ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
start_download_butt = ttk.Button(frm, text='Start Download', command=butt_click).grid(column=0, row=1)
stop_download_butt = ttk.Button(frm, text='Stop Download').grid(column=1, row=1)
quit_butt = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()