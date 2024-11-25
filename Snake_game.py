import turtle
import random
import time
sc=0
hs=0
delay=0.1
bodies=[]

#Creating a Screen

s1=turtle.Screen()
s1.bgcolor("light blue")
s1.title("Snake Game")
s1.setup(width=600,height=600)

#Creating a Head

head=turtle.Turtle()
head.shape("circle")
head.color("red")
head.fillcolor("yellow")
head.penup()
head.goto(0,0)
head.speed(0)
head.direction="stop"

#Creating a Food

food=turtle.Turtle()
food.shape("turtle")
food.color("green")
food.penup()
food.ht()
food.goto(200,250)
food.st()
food.speed(0)

#Creating Score Board
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-280,280)
sb.write("Score:0 | Highest Score:0")

#Creating Function for Moving in all Direcrions
def moveUp():
    if head.direction!="down":
        head.direction="up"
def moveDown():
    if head.direction!="up":
        head.direction="down"

def moveRight():
    if head.direction!="left":
        head.direction="right"
def moveLeft():
    if head.direction!="right":
        head.direction="left"
def moveStop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#Event Handling
s1.listen()
s1.onkey(moveUp,"Up")
s1.onkey(moveDown,"Down")
s1.onkey(moveLeft,"Left")
s1.onkey(moveRight,"Right")
s1.onkey(moveStop,"space")

#MainLoop
try:
    while True:
        s1.update()
        #Check collision with border
        if head.xcor()>290:
            head.setx(-290)
        if head.ycor()>290:
            head.sety(-290)
        if head.xcor()<-290:
            head.setx(290)
        if head.ycor()<-290:
            head.sety(290)

#Check Collision with food

        if head.distance(food)<20:
            x=random.randint(-290,290)
            y=random.randint(-290,290)
            food.goto(x,y)
            #Increasing size of Snake
            body=turtle.Turtle()
            body.speed(0)
            body.penup()
            body.shape("circle")
            body.color("red")
            body.fillcolor("green")
            bodies.append(body)
            sc=sc+10
            delay=delay-0.001
            if sc>hs:
                hs=sc
            sb.clear()
            sb.write("Score:{} | Highest Score:{}".format(sc,hs))
#move snake bodies
        for i in range(len(bodies)-1,0,-1):
            x=bodies[i-1].xcor()
            y=bodies[i-1].ycor()
            bodies[i].goto(x,y)
        if len(bodies)>0:
            x=head.xcor()
            y=head.ycor()
            bodies[0].goto(x,y)
        move()
#Check Collision with snake body
        for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction="stop"
                for body in bodies:
                    body.ht()
                bodies.clear()
                sc=0
                delay=0.1
                sb.clear()
                sb.write("Score:{} | Highest Score:{}".format(sc,hs))
        time.sleep(delay)
    s1.mainloop()
except:
    print("Game Over")

        
        
        
    
    



