from tkinter import *
from tkinter import ttk
root=Tk()
root.title('NS')
root.geometry('470x340')

#titel
titel= Label(root, text='Welkom in het station',font='calibre 20 bold')
titel.grid(row=0,column=0,pady=10,columnspan=2)


#first and last name
frame= Label(root,text='U mening')
frame.grid(row=1,column=0)

entry=Entry(root,width=20)
entry.grid(row=1,column=1,sticky='we')

def record():
    r = frame.get()
    y = r
    with open('Ns-bericht.csv') as file:
        file.write(y)




button=Button(root,text='Verzenden',command=record)
button.grid(row=6,column=3,padx=10,sticky='w')

root.mainloop()