from pygame_functions import *
import random

screenSize(1000,900)
#setBackgroundColour("darkgreen")
setAutoUpdate(False)

class Ball:
    def __init__(self,x,y, colour): # __init__ is a constructor
        # attributes (somtimes called properties)
        self.xPos = x
        self.yPos = y
        self.colour = colour # encapsulation
        self.ySpeed = random.randint(-10,10)
        self.xSpeed = random.randint(-10,10)
    
    #methods - functions#
    def move(self):
        self.ySpeed += 1
        self.xPos += self.xSpeed
        self.yPos += self.ySpeed
        if(self.yPos > 900):
            self.ySpeed *= -1
            self.yPos = 900
        if(self.xPos < 0):
            self.xSpeed *= -1
            self.xPos = 0
        elif(self.xPos > 1000):
            self.xSpeed *= -1
            self.xPos = 1000
        drawEllipse(self.xPos,self.yPos,50,50,self.colour)
        

colours = ["red","orange","blue","white","purple"]
balls = [Ball(random.randint(50,850),random.randint(50,950),(random.randint(0,255),random.randint(0,255),random.randint(0,255))) for i in range(500)]

while(True):
    for b in balls:
        b.move()
    
    tick(60)
    updateDisplay()
    clearShapes()

endWait()