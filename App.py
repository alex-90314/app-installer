import os
from tkinter import *
from tkinter import ttk

import requests
from bs4 import BeautifulSoup

from urls import url_list

root = Tk()
os.system("cls")
#sets the button click to run code
def butt_click():
    os.system("cls")
    os.system('code()')

#setting up the frame
frm = ttk.Frame(root, padding=10)
frm.grid()

#setting up start & stop buttons
hello_label = ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
start_download_butt = ttk.Button(frm, text='Start Download', command=butt_click).grid(column=0, row=1)
stop_download_butt = ttk.Button(frm, text='Stop Download').grid(column=1, row=1)
quit_butt = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()

def code():
    for i in range(len(url_list)):
        url = url_list[i]
        print(url)
    '''    response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        list_element = ""

        elements = soup.find_all("div", class_="hJDwNd-AhqUyc-II5mzb")  # Replace "class-name" with the actual class name you want to target
        for element in elements:
            list_element.append(element)

        for i in range(len(list_element)):
            while len(list_element) > 1:
                list_element.pop(0)

        print(list_element)'''