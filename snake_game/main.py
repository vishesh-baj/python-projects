from turtle import Screen
import time
from snake import Snake
from food import Food

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

# creating snake instance on screen
snake = Snake()
# food 
food = Food()

# to listen to key events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right") 
game_over = False 

while not game_over:
    screen.update()
    time.sleep(.1)

    # Move snake forward
    snake.move_snake()   

    # collision with food 
    if snake.head.distance(food) < 15:
        print("Collided")
        food.refresh()
# exit on click
screen.exitonclick()
