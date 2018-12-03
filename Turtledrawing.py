"""Made by Kousik Rajesh  """
from turtle import*
from tkinter import*
root=Tk()
width(5)

shape("turtle")
left(90)

def tup():
   
    seth(90)
    while True:
        fd(1)
def tleft():
    
    seth(180)   
    
    while True:
        fd(1)
def tdown():
    seth(270)
    while True:
        fd(1)
def tright():
    
    seth(0)
    while True:
        fd(1)
def fineadjust():
    fd(1)
def stop():
     while True:
        lt(1)
        undo()
    
def tantclock():
    
    
    while True:
        lt(1)
def tclock():
    
    
    while True:
        rt(1)
def move():
    
    
    while True:
        fd(1)
def tundo():
    while True:
        undo()
def close():
    bye()
           
up=Button(root,text="UP",command=tup).pack()

left=Button(root,text="LEFT",command=tleft).pack()
right=Button(root,text="RIGHT",command=tright).pack()
down=Button(root,text="DOWN",command=tdown).pack()
fineadjust=Button(root,text="FINE ADJUST",command=fineadjust).pack()
stop=Button(root,text="STOP",command=stop).pack()
tantclock=Button(root,text="TURN ANTICLOCKWISE",command=tantclock).pack()
tclock=Button(root,text="TURN CLOCKWISE",command=tclock).pack()
move=Button(root,text="MOVE",command=move).pack()
tundo=Button(root,text="UNDO",command=tundo).pack()
close=Button(root,text="QUIT",command=close).pack()

root.mainloop()

