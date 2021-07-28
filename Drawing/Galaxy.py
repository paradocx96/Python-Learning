import turtle
import random

class MyTurtle(turtle.Turtle):
    # a square with an initial angle of x and a side length of x
    def draw_square(self, x):
        self.setheading(x)
        for i in range(4):
            self.forward(x)
            self.left(90)
        return
    # Randomly get the three parameters of the color in rgb mode
    def get_color(self):
        rgb = []
        for i in range(3):
            rgb.append(random.randint(0, 255))
        return rgb
    #Set the color of the brush
    def set_pen_color(self):
        self.screen.colormode(255)
        self.pencolor(self.get_color())

t = MyTurtle()
t.screen.bgcolor("black")
t.speed(0)

# traverse all angles from 1 to 1000°, as the initial angle increases, the side length of the square also increases.
x = 1
while x < 1000:
    t.set_pen_color()
    t.draw_square(x)
    x = x + 1

t.screen.mainloop()
