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
        self.ySpeed = 10
        self.xSpeed = 8
    
    #methods - functions#
    def move(self):
        self.xPos += self.xSpeed
        self.yPos += self.ySpeed
        if(self.yPos > 900):
            self.ySpeed *= -1
            self.yPos = 900
        elif(self.yPos < 0):
            self.ySpeed *= -1
            self.yPos = 0
        if(self.xPos < 0):
            self.xSpeed *= -1
            self.xPos = 0
        elif(self.xPos > 1000):
            self.xSpeed *= -1
            self.xPos = 1000
        drawEllipse(self.xPos,self.yPos,26,26,self.colour)

class Brick:
    def __init__(self,x,y, colour):
        self.xPos = x
        self.yPos = y
        self.colour = colour
        self.width = 75
        self.height = 50
    
    def draw(self):
        drawRect(self.xPos,self.yPos,self.width,self.height,self.colour)
    
    
    def hit(self,ball):
        if(self.xPos <= ball.xPos <= self.xPos + self.width):
            if(self.yPos <= ball.yPos <= self.xPos + self.height):
                return True
        
        return False
    
    def update(self,ball):
        self.draw()
        print(self.detectHit(ball))
        
    
        
            
        
        

balls = []
balls.append(Ball(500,500,"red"))
bricks = []
for x in range(0,1000,77):
    bricks.append(Brick(x,100,"orange"))
    bricks.append(Brick(x,200,"red"))
    bricks.append(Brick(x,300,"green"))
    

while(True):
    for b in balls:
        b.move()
    for brick in bricks:
        brick.draw()
    
    
    tick(60)
    updateDisplay()
    clearShapes()

endWait()
