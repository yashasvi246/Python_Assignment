import tkinter
from tkinter import *

window=tkinter.Tk()
window.title('GUI')
def GUI_Tutorial():
      
      label=tkinter.Label(window,text='Hello Yashasvi!!').pack()
tkinter.Button(window,text='Click Me',command=GUI_Tutorial).pack()
window.mainloop()
