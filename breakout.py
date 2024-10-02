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
        self.acc = 1
        
    
    #methods - functions#
    def move(self):
        global lives
        if(self.acc > 1.5):
            self.acc = 1.5
        
        self.xPos += (self.xSpeed*self.acc)
        self.yPos += (self.ySpeed*self.acc)
        if(self.yPos > 900):
            self.ySpeed *= -1
            self.yPos = 700
            self.xPos = 500
            lives -= 1
            self.acc = 1
            
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
        self.height = 30
        self.active = True
    
    def draw(self):
        if(self.active):
            drawRect(self.xPos,self.yPos,self.width,self.height,self.colour)
    
    
    def hit(self,balls):
        for ball in balls:
            if(self.xPos <= ball.xPos <= self.xPos + self.width):
                if(self.yPos <= ball.yPos <= self.yPos + self.height):
                    ball.ySpeed *= -1
                    ball.acc += 0.1
                    return True
            
            
    
    def update(self,ball):
        global totalBricks
        self.draw()
        
        if(self.active and self.hit(ball)):
            self.active = False
            totalBricks -= 1
            
            
        
    
class Bat(Brick): #inherits brick class - called inheritance, bat is subclass of brick
    def __init__(self,x,y,colour):
        super().__init__(x,y,colour)
        self.width = 100
        self.height = 25
    
    def update(self,balls): # overriding the previous
        self.draw()
        self.hit(balls)
        self.xPos = mouseX()
        """
        if(keyPressed("right") and self.xPos < 900):
            self.xPos += 10
        if(keyPressed("left") and self.xPos > 0):
            self.xPos -= 10
        """

class MultiBrick(Brick):
    def update(self,balls):
        global totalBricks
        self.draw()
        if(self.active and self.hit(balls)):
           self.active = False
           totalBricks -= 1
           balls.append(Ball(self.xPos,self.yPos,"blue"))


balls = []
balls.append(Ball(500,500,"red"))
bricks = []
for x in range(0,1000,77):
    bricks.append(Brick(x,100,"orange"))
    bricks.append(Brick(x,200,"red"))
    bricks.append(Brick(x,300,"green"))

randomPos = random.randint(0,len(bricks))
removedbrick = bricks.pop(randomPos)
bricks.insert(randomPos,MultiBrick(removedbrick.xPos,removedbrick.yPos,"salmon"))
    
totalBricks = len(bricks)

bat = Bat(500,850,"lightblue") # an instance of the bat - instantiation
lives = 3

livesLabel = makeLabel("Lives: "+str(lives),24,10,10,"white")
gOLabel = makeLabel("Game Over!",50,380,450,"red")
showLabel(livesLabel)

running = True

while(running):
    if(lives <= 0 or totalBricks <= 0):
        showLabel(gOLabel)
        running = False
    bat.update(balls)
    for b in balls:
        b.move()
    for brick in bricks:
        brick.update(balls)
    
    
    tick(60)
    updateDisplay()
    clearShapes()
    changeLabel(livesLabel,"Lives: " + str(lives))

endWait()

