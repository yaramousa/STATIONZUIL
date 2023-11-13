from tkinter import *
def myfunction():
    exit()

myframe= Tk()
myframe.title('My app')
myframe.geometry()

mylabel=Label(myframe,text='web browser',font='tahoma 20 bold')
mylabel.pack(pady=30)
mytext= Entry(myframe,width=50)
mytext.pack(pady=10)

mybutton= Button(myframe,text='click me',fg='blue',bg='yellow',font='helvatica 10 bold',pady=10,padx=3,command=exit)
mybutton.pack()



myframe.mainloop()
