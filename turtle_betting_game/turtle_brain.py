import turtle

class TurtleBluePrint:
    def __init__(self, color):
        self.color = color

    def create_turtle(self):
        t = turtle.Turtle()
        t.color(self.color)
        return t


