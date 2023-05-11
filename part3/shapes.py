import math 

class rectangle:
    def __init__(self):
        self.width = 12
        self.height = 7
    
    def calculateArea(self):
        return self.width * self.height

class circle:
    def __init__(self):
        self.radius = 5
    
    def calculateArea(self):
        return math.pi * self.radius * self.radius


def printArea(shape):
    print(shape.calculateArea())

rec = rectangle()
cir = circle()
printArea(rec)
printArea(cir)
