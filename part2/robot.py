class Robot:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0

    def showPosition(self):
        print("The robot is at", self.xpos, self.ypos)
    
    def moveUp(self):
        self.ypos= self.ypos+ 1
    
    def moveDown(self):
        self.ypos= self.ypos- 1

walle = Robot()
walle.moveDown()
walle.moveDown()
walle.showPosition()