import secrets
import string,time
import tkinter,threading
from tkinter import Entry,messagebox,LEFT,StringVar
from tkinter import filedialog,ttk,Text
import os
from tkinter import Toplevel
from datetime import datetime
def passgen(_event=None):
    global passwor
    passwor=''
    cha="qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM1234567890?"
    e1=Entry.get(e)
    ch=len(e1)
    if(ch==0 or e1=="0" or e1 not in string.digits):messagebox.showwarning("warning","Length cannot be zero")
    else:pass
    print(ch)
    e2=int(e1)
    print(ch)
    for i in range(e2):
        passwor+=secrets.choice(cha)
        a2.config(text=passwor,font="Helvetica 22 italic",fg="red")
def time1():
           #a=datetime.now().strftime("%I:%M:%S:%f:%p")
           a=time.strftime("%I:%M:%S")
           l234.config(text=a,font="Helvetica 15 italic",fg="green")
           window.update_idletasks()
           window.after(1,time1)
def savep():
    global e212
    top=Toplevel()
    top.geometry("200x200")
    top.title("Saving file")
    l21=tkinter.Label(top,text="Enter the name of file")
    l21.pack()
    e212=tkinter.Entry(top)
    e212.pack()
    b21=tkinter.Button(top,text="done",command=savep1,activeforeground="red",relief="groove")
    b21.pack()
    top.mainloop()
def savep1():
    e22=e212.get()
    f12=filedialog.askdirectory()
    os.chdir(f12)
    f1=open(e22,"w+")
    f1.write(passwor)
    f1.close()
    b23=tkinter.Button(frame,text="quit",command=window.destroy)
    b23.pack()
def tracer(a,b,c):
    passgen()
window=tkinter.Tk()
window.title("Password Generator")
var=StringVar()
var.trace('w',tracer)
frame=tkinter.Frame(window)
frame.pack()
text=tkinter.Text()
a=tkinter.Label(frame,text="Password Generator",font="Helvetica 33 bold",fg="green")
a.pack()
a1=tkinter.Label(frame,text="Enter the length of your password",font="Helvetica 15 italic",fg="red")
a1.pack()
e=tkinter.Entry(frame,textvariable=var)
e.focus()
e.bind('<Return>',passgen)
e.pack()
b=tkinter.Button(frame,command=passgen,text="generate",activebackground="green",relief="ridge")
b.pack()
b1=tkinter.Button(frame,text="save",command=savep,activebackground="lightgreen",relief="groove")
b1.pack()
a2=tkinter.Label(text="")
a2.pack()
l234=tkinter.Label(frame,text="")
l234.pack()
t1=threading.Thread(target=time1)
t1.start()
window.mainloop()
