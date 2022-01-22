from turtle import Screen, Turtle
import time
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

initial_cords = [(0,0),(-20,0),(-40,0)]
segments_list = []
for position in initial_cords:
    segment = Turtle('square')  
    segment.pensize(10)
    segment.color('white')
    segment.penup()
    segment.goto(position)

    segments_list.append(segment) 


game_over = False 

while not game_over:
    screen.update()
    time.sleep(.1)


    for segment_num in range(len(segments_list) -1,0,-1):
        new_x = segments_list[segment_num - 1].xcor()
        new_y = segments_list[segment_num - 1].ycor()
        segments_list[segment].goto(new_x,new_y)
    segments_list[0].forward(20)
    segments_list[0].left(90)

         

    


# exit on click
screen.exitonclick() 
