#!/bin/env python3

import os
import sys
import time
from tkinter import *
from tkinter import filedialog
import hashlib

class pickrpt:
    def chg_pphrase(o, event):
        o.l_sz['text'] = hashlib.sha512(o.e_pphrase.get().encode("utf-8")).hexdigest()

    def select_pic(o):
        o.pic = filedialog.askopenfilename(initialdir = ".",title = "Select BMP file",filetypes = (("BMP files","*.bmp"),("all files","*.*")))
        if o.pic == '':
            return
        print(o.pic)
        o.l_selectpic['text'] = "Image file: "+o.pic

    def __init__(o):
        o.root = Tk()
        o.root.title('Pic Crypt')
        o.root.geometry('500x600')

        # Tkinter elements
        o.l_text = Label(o.root, text='Message:')
        o.e_text = Text(o.root)
        o.b_selectpic = Button(o.root, text='Select carrier file', command=o.select_pic)
        o.l_selectpic = Label(o.root, text='')
        o.e_pphrase = Entry(o.root, text='Passphrase')
        o.l_sz = Label(o.root, text='', wraplength=300)

        # Tkinter event bindings
        o.e_pphrase.bind('<KeyRelease>' , o.chg_pphrase)

        # Tkinter grid
        o.l_text.grid(row=0, column=0)
        o.e_text.grid(row=1, column=0)
        o.b_selectpic.grid(row=2, column=0)
        o.l_selectpic.grid(row=3, column=0)
        o.e_pphrase.grid(row=4, column=0)
        o.l_sz.grid(row=5, column=0)

        o.root.mainloop()

frame=pickrpt()