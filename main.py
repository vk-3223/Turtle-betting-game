from turtle import Screen, Turtle
import random
import turtle

is_race_on = False
screen = Screen()

screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "make your bet",prompt="which tutle win the race")
colours = ["red","orange","yellow","blue","green","purple"]
y_postion = [-70,-40,-10,20,50,80]
all_turtle = []
for turtule_index in range(0,6):
    timy_the_turtle = Turtle(shape="turtle")
    timy_the_turtle.penup()
    timy_the_turtle.color(colours[turtule_index])
    timy_the_turtle.goto(x=-230,y=y_postion[turtule_index])
    all_turtle.append(timy_the_turtle)
if user_bet:
    is_race = True
while is_race:
   
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"you win the race {wining_color}")
            else:
                print(f"you are lose and this race win is {wining_color} turtle")    
        random_distant =  random.randint(0,10)    
        turtle.forward(random_distant)
screen.exitonclick()