from tkinter import *
import math, time, random
from window import window

w = window()

#Angle for turning the branches
angle = 2/15 * math.pi

#Where is the root of the tree in the screen
startPosition = [350, 700]

#By what percentage should the length decrease by should be between (0,1)
shrinkingFactor = 0.7

#The starting length of the first branch
length = 140

#Initial direction as a vector
#This vector points straight up
initialDirection = [0, -1]

#If the branch length is smaller than this then stop 
stoppingLength = 2

def rotate(vec, theta):
    return [vec[0]*math.cos(theta)-vec[1]*math.sin(theta), vec[0]*math.sin(theta)+vec[1]*math.cos(theta)]

def branch(len, pos, dir, w):
    if len < stoppingLength:
        return
    newpos = [pos[0]+len*dir[0], pos[1]+len*dir[1]]
    w.line(pos[0], pos[1], newpos[0], newpos[1])
    branch(len * shrinkingFactor, newpos, rotate(dir,  angle), w)
    branch(len * shrinkingFactor, newpos, rotate(dir, -angle), w)
    w.update() # Delete this line to speed it up
    
branch(length, startPosition, initialDirection, w)
w.update()
w.keep()
