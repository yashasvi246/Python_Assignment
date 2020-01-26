import tkinter.messagebox
from tkinter import *

window=tkinter.Tk()
window.title('GUI')


tkinter.messagebox.showinfo('Alert message','This is just a alert message')
response=tkinter.messagebox.askquestion('Tricky Question','Do you love Deep Learning??')
if response=='yes':
      tkinter.Label(window,text='Yes ,Offcourse Deep learning').pack()
else:
      tkinter.Label(window,text='No ,I dont love Deep learning').pack()
      
window.mainloop()
