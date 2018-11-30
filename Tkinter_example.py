

#Importing tkinter and all its packages
import tkinter
from tkinter import *

#Importing Time Library
import time

#Importing Math Library
import math

#Import Random Library for "spinning wheel"
import random

#Setting up tkinter workspace and naming it top
top = Tk()

#Setting up Canvas and naming it C
C = tkinter.Canvas(top, bg="blue", height=600, width=600)
C.pack()


#Setting up vertices for white small rectangles
x1 = x2 = 0
y1 = y4 = 40
y2 = y3 = 90
x3 = x4 = 300

#For loop prints 10 white rectangles on left of canvas 
for i in range(0,11):
    rectangle = C.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = "white")
    y1 = y1+51
    y2 = y2+51
    y3 = y3+51
    y4 = y4+51
    
#Used as dimensions for printing text in white boxes
xt = 150
yt = 70

#Printing Title Text
C.create_text(320,20,fill="white",font="Times 20 bold",
                    text="rishabh kemni is bad at making decisions")


#Array to store text for boxes
array = ['Samosa', 'Aloo parantha', 'Pizza', 'Noodles', 'Burger','Paneer-roti','Pav- Bhaji','Kisi ka Dimaag','Coffee- Biscuit','CHOLE BHATURE','FAST TODAY']


#For loop prints text in each box based on above array and above dimensions
for n in range(0,11):
    C.create_text(xt,yt,fill="black",font="Times 20 italic bold",
                        text=array[n])
    yt = yt+50
    
    

#Function called when button pushed that "spins the wheel" and picks a block
def spin():
    #This for loop clears the screen
    x1 = x2 = 300
    y1 = y4 = 40
    y2 = y3 = 90
    x3 = x4 = 650
    for b in range(0,13):
        rectangle = C.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = "blue")
        y1 = y1+51
        y2 = y2+51
        y3 = y3+51
        y4 = y4+51
        
    #This creates the gold rectangle
    rectangle = C.create_polygon(300,40,300,90,550,90,550,40, fill = "gold")
    
    #Creating the random number to "spin the wheel"
    x = random.randint(20,40)
    
    #yd is used to move spin the wheel by moving the gold box up and down by distance yd
    yd = 51
    
    #This loop "spins the wheel" by moving the gold box up and down, and if it hits the top
    # or bottom it bounces back up by reversing the direction of yd
    for i in range (0,x):
        
        C.move(rectangle,0,yd)
        p=C.coords(rectangle)
        if p[3] >= 550 or p[5] >= 550:
            yd = -yd
        elif p[1] <=90 or p[3] <= 90:
            yd = -yd
        top.update()
        time.sleep(0.06)
    
#Function not being currently used but clears right side of board and makes all rectangles blue
def reset():
    x1 = x2 = 300
    y1 = y4 = 0
    y2 = y3 = 50
    x3 = x4 = 650
    for i in range(0,13):
        rectangle = C.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = "blue")
        y1 = y1+51
        y2 = y2+51
        y3 = y3+51
        y4 = y4+51
    
    
    

#Setting up Spin Button
B = tkinter.Button(top, text ="Spin", command = spin)
B.pack()



#Running main program for Tk workspace
top.mainloop()
