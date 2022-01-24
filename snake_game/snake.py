# snake class 
from turtle import Turtle

START_CORDS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

 
class Snake:
    def __init__(self):
        self.initial_cords = START_CORDS
        self.segments_list = []
        # calling this method once the snake object is instanciated 
        self.draw_snake()
        self.head = self.segments_list[0]
    


    def draw_snake(self):
        for position in self.initial_cords:
            segment = Turtle('square')  
            segment.pensize(10)
            segment.color('white')
            segment.penup()
            segment.goto(position)

            self.segments_list.append(segment) 
    
    def move_snake(self):
        for segment_num in range(len(self.segments_list) - 1, 0, -1):
            new_x_cord = self.segments_list[segment_num -1].xcor()
            new_y_cord = self.segments_list[segment_num - 1].ycor()

            self.segments_list[segment_num].goto(new_x_cord,new_y_cord)
             
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)    

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def sight(self):
        print("Ask specifics! ")
        print("Specific construct of the self analysis of this world ! ")

    def signht_specific_1(self):
        print("Syntax sugar")





    

            


