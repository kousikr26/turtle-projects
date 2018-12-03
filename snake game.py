
"""Game using turtle module on python
Use arrow keys to move
Time limit : 15 sec"""

from turtle import *

import random
import time
pu()
setpos(-300,-300)
pd()
lt(90)
fd(600)
rt(90)
fd(600)
rt(90)
fd(600)
rt(90)
fd(600)
pu()
setpos(0,0)
pu()

bgcolor("cyan")


n=False
speed("fastest")
width(5)
starttime=time.time()
score=0
file=open("highscore.txt","r+")
highscore=int(file.read())

class plottarget:
    def __init__(self):
        self.targx=random.randint(-290,290)
        self.targy=random.randint(-290,290)
    def plot(self):
        self.a=xcor()
        self.b=ycor()
        setpos(self.targx,self.targy)
        shape("circle")
        self.stam=stamp()
        shape("turtle")
        setpos(self.a,self.b)
target=plottarget()
target.plot()


def removetarget():
    global n,target,score
    if xcor()>target.targx-10 and xcor()<target.targx+10 and ycor()>target.targy-10 and ycor()<target.targy+10:
        clearstamp(target.stam)
        if n==False:
            target=plottarget()
            target.plot()
            n=True
            score+=1
            
        
    else:
        n=False
        pass
        
        
    



left(90)
def inpu():
    x=xcor()
    y=ycor()
    currtime=time.time()
    if currtime-starttime<=15:
        pass
    else:
        print("Game over")
        print("Your score:",score)
        print("High score:",highscore)
        temp=input()
        n=False
        if score>highscore:
            file.write(str(score))
            file.close()
        quit()
        temp=input()
    if x>-300.0 and x<300.0 and y>-300.0 and y<300.0:
        return True
    else:
        if x>=300.0:
            setpos(-300.0,y)
        elif x<=-300.0:
            setpos(300.0,y)
        elif y>=300.0:
            setpos(x,-300.0)
        elif y<=-300.0:
            setpos(x,300.0)
        return True    
                
            
    def tup():
    
    
    seth(90)
    while inpu():
        removetarget()
        fd(2)
        
    
def tleft():
    
    seth(180)
    
    while inpu():
        removetarget()
        fd(2)
def tdown():
    seth(270)
    while inpu():
        removetarget()
        fd(2)
def tright():
    
    seth(0)
    while inpu():
        removetarget()
        fd(2)

onkey(tup,"Up")
onkey(tright,"Right")
onkey(tleft,"Left")
onkey(tdown,"Down")


listen()
mainloop()

