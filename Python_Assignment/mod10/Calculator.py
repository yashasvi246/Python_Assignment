import tkinter

def btn_clear(item):
      global expression
      expression=''
      input_text.set('')
def btn_click():
      global expression
      expression=expression+str(item)
      input_text.set(expression)
def btn_equal():
      global expression
      result=str(eval(expression))
      input_set.set(eval(expression))
      expression=''
expression=''
input_text=StringVar()
input_frame=Frame(window,width=312,height=50,bd=0,highlightb)
input_frame.pack(side=Top)
input_field=Entry(input_frame,font=('arial',10,'bold'),textvaris)
input_field.grid(row=0,column=0)
btns_frame=Frame(window,width=312,height=272.5,bg='grey')
btns_frame.pack()

clear=Button(btns_frame,text='c',fg='black',width=32,height=50)
divide=Button(btns_frame,text='',fg='black',width=10,height=50)
