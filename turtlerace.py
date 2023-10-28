

from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500 , height=400)


colors = ["red","blue","green"]
k = -50
all_turtles = []
for i in colors:
    name = i
    name = Turtle()
    name.color(i)
    name.penup()
    name.goto(-200,k)
    k=k+50
    all_turtles.append(name)

user_bet = screen.textinput(title = "make your bet", prompt = "which will win the race")
print(user_bet)

if user_bet: 
    is_race_on = True

def race_start(is_race_on):
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor()>230:
                is_race_on = False
                # print((turtle.pencolor())+" won")
                tx = Turtle()
                tx.hideturtle()
                tx.write(turtle.pencolor() + " won", align= "center", font=("monospace", 30, "bold"))

            t1 = random.randint(0,10)
            turtle.forward(t1)

   
    


race_start(is_race_on)
screen.exitonclick() 


