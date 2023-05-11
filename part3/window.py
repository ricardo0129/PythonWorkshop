from tkinter import *

class window:
    def __init__(self):
        self.win=Tk()
        self.win.geometry("1000x1000")
        self.canvas=Canvas(self.win, width=1000, height=1000)
        self.canvas.pack()

    def line(self, x1, y1, x2, y2, fill="gray"):
        self.canvas.create_line(x1, y1, x2, y2, fill=fill, width=2)
    
    def circle(self, x1, y1, r, fill = "green"):
        self.canvas.create_oval(x1-r, y1-r, x1+r, y1+r, fill = fill)
    
    def update(self):
        self.win.update_idletasks()
        self.win.update()

    def clear(self):
        self.canvas.delete("all")
    
    def keep(self):
        self.win.mainloop()
