import tkinter as tk

class SimpleGraphics(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg='white', **kwargs)
        self.bind('<Button-1>', self.draw_circle)

    def draw_circle(self, event):
        r = 20
        x, y = event.x, event.y
        self.create_oval(x - r, y - r, x + r, y + r, fill='steelblue', outline='black')
