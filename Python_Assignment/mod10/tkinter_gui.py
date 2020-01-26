import tkinter
window=tkinter.Tk()
#to rename the title of the window
window.title('GUI')
#pack is used to show the object in the window
label=tkinter.Label(window,text='Welcome to GUI').pack()
button_widget=tkinter.Button(window,text='Welcome to Button')
button_widget.pack()
top_frame=tkinter.Frame(window).pack()
bottom_frame=tkinter.Frame(window).pack(side='bottom')
#fg will change the foreground Color
btn1=tkinter.Button(top_frame,text='Button1',fg='red').pack()
btn2=tkinter.Button(bottom_frame,text='Button2',fg='green').pack()
btn3=tkinter.Button(bottom_frame,text='Button3',fg='blue').pack()
btn4=tkinter.Button(bottom_frame,text='Button4',fg='pink').pack()

tkinter.mainloop()
window.mainloop()
