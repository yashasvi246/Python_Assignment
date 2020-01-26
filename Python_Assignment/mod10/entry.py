import tkinter
from tkinter import *
window=tkinter.Tk()
window.title('GUI')
label=tkinter.Label(window,text='username').grid(row=0,sticky=W)
tkinter.Entry(window).grid(row=0,column=1)
label=tkinter.Label(window,text='password').grid(row=1,sticky=W)
tkinter.Entry(window).grid(row=1,column=1)
tkinter.Checkbutton(window,text='Keep me logged in').grid(columnspan=2)
window.mainloop()
