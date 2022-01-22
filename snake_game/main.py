from turtle import Screen, Turtle
import time
from snake import Snake


# screen configuration
screen = Screen()
# screen resolution
screen.setup(width=600,height=600)
# screen background color
screen.bgcolor('teal')
# screen title 
screen.title("Snake Game") 
# turning off tracer 
screen.tracer(0)

# creating snake instance 
snake = Snake()

# drawing snake on screen
snake.draw_snake()

game_over = False 

while not game_over:
    screen.update()
    time.sleep(.1)

    # Move snake forward
    snake.move_snake()   
# exit on click
screen.exitonclick() 
