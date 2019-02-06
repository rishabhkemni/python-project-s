import tkinter
import platform
import winsound
from tkinter import ttk,messagebox,LEFT,END
from tkinter import Entry,Label
from platform import uname
from winsound import Beep
global a,e,e2
e=''
e2=''
a=''
a=platform.uname()[0]
print(a)
def fun3():
    e11=Entry.get(e)
    e12=Entry.get(e2)
    m1=int(e11)
    m2=int(e12)
    Beep(m1,m2)
def fun4():
    e.delete(0,END)
    e2.delete(0,END)
window=tkinter.Tk()
window.title("Sound Generator")
l=Label(window,text="Enter the frequency in Hertz(37Hz-32767Hz)",font="Helvetica 15 italic",fg="green")
e=Entry()
e.focus()
l2=Label(window,text="Enter time in milli seconds",font="Helvetica 15 italic",fg="green")
e2=Entry()
b=ttk.Button(window,text="Generate",command=fun3)
b1=ttk.Button(window,text="clear",command=fun4)
l.pack()
e.pack(padx=10,pady=10)
l2.pack()
e2.pack(padx=60,pady=10)
b.pack(padx=90,side=LEFT)
b1.pack(padx=15,side=LEFT)
window.mainloop()

