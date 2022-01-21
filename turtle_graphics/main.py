import turtle as t
import random

t.colormode(255)
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('teal')
colors = ['teal','red','yellow','blue','crimson','green','lime']
def move_and_turn_right():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

# for i in range(4):
#     move_and_turn_right()

def draw_dashed_line():
   for _ in range(15):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


def create_shape(sides, direction):
    angle = 360/sides
    for i in range(sides):
        timmy_the_turtle.forward(100)
        if direction == 'right':
            timmy_the_turtle.right(angle)
        else: 
            timmy_the_turtle.left(angle)


# for i in range(3,11):
#     timmy_the_turtle.color(random.choice(colors))
#     create_shape(i,'right')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tupple = (r,g,b)
    return color_tupple

def random_path():
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.speed(0)
    while True:
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.forward(20)
        random_direction = random.choice([0,90,180,270])
        timmy_the_turtle.setheading(random_direction)


# tuple 
my_tuple = (1,3,4,5,6)


def draw_circle(radius):
    angle = 0
    while angle <= 360:
        angle += 10
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(radius)
        timmy_the_turtle.setheading(angle)




   









# random_path()
draw_circle(80)



screen = t.Screen()
screen.exitonclick()
