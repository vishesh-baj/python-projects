from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("make your bet", "which turtle will win the race? Enter color: ")

is_race_on = False

turtle_list = []
for i in range(0,6):
    y_cord = [-70,-40,-10,20,50,80]
    colors = ['red','green','blue','orange','indigo','teal']
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,y_cord[i])
    turtle_list.append(new_turtle)

user_bet_amount = int(input("Enter the betting amount: "))
percentage_won = 2



if user_bet:
    is_race_on = True
     
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()  
            if winning_color == user_bet:
                print(f'Your selected color {user_bet} won! You have {user_bet_amount * percentage_won} points')
                is_race_on = False
            else:
                print(f'Your selected color {user_bet} lost, wining color is {winning_color}')
                is_race_on = False

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


    

 
screen.exitonclick()
