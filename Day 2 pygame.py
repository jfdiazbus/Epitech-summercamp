import random
from math import cos, pi, sin
import time
import turtle
BOUNDARYx = 640
BOUNDARYy = 340
wn=turtle.Screen()
wn.title("My first game")
wn.bgcolor("black")
wn.setup(width=1300,height=700)
wn.tracer(0)
player=turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0,-250)


def init_enemies():
    es=[]
    for i in range(5):
        enemy=turtle.Turtle()
        enemy.shape("triangle")
        enemy.color("green")
        enemy.penup()
        enemy.speed(0)
        x=int(random.randint(-600,600))
        y=int(random.randint(-300,300))
        angle=int(random.randint(0,360))
        rad=angle*pi/180
        x_offset = cos(rad)
        y_offset = sin(rad)
        enemy.setx(x + x_offset * 2)
        enemy.sety(y + y_offset * 2)
        es.append(enemy)
    return es

enemies = init_enemies()

def move_up():
    speed_y = 20
    if player.ycor()==340:
        speed_y=0
    player.xcor()
    player.sety(player.ycor()+speed_y)
def move_down():
    speed_y = -20
    if player.ycor()==-340:
        speed_y=0
    player.ycor()
    player.sety(player.ycor()+speed_y)
def move_left():
    speed_x = -20
    if player.xcor()==-640:
        speed_x=0
    player.xcor()
    player.setx(player.xcor()+speed_x)
def move_right():
    speed_x = 20
    if player.xcor()==640:
        speed_x=0
    player.xcor()
    player.setx(player.xcor()+speed_x)
    
wn.listen()
wn.onkey(move_up,"Up")
wn.onkey(move_down,"Down")
wn.onkey(move_left,"Left")
wn.onkey(move_right,"Right")


def runGame():
    run=True
    while run:
        for enemy in enemies:
            angle=int(random.randint(1,360))
            rad=angle*pi/180
            x_offset = cos(rad)
            y_offset = sin(rad)

            enemy.setx(enemy.xcor() + x_offset * 2)
            enemy.sety(enemy.ycor() + y_offset * 2)

            if player.distance(enemy)<20:
                player.goto(0,-250)
                n+=n
                
                if n==3:
                    run=False

        wn.update()
        turtle.delay(100)

runGame()