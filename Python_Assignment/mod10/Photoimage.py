import tkinter
window=tkinter.Tk()
window.title('GUI')
icon=tkinter.PhotoImage(file= 'C:\\Users\\Student\\Desktop\\card.png')
label1=tkinter.Label(window,image=icon)
label1.pack()
window.mainloop()
