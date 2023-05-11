class Robot:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.robotName = "Wall-E"

    def showPosition(self):
        print("The robot is at", self.xpos, self.ypos)
    
    def moveUp(self):
        self.ypos = self.ypos + 1
    
    def moveDown(self):
        self.ypos = self.ypos - 1

    def moveLeft(self):
        self.xpos = self.xpos - 1

    def moveRight(self):
        self.xpos = self.xpos + 1

    def printName(self):
        print(self.robotName)

walle = Robot()

for i in range(1000):
    walle.moveDown()

for i in range(200):
    walle.moveRight()

walle.showPosition()

walle.printName()
