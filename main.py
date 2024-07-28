from turtle import* 
from random import* 
width=200 
height=250 
t1=Turtle() 
t2=Turtle() 
t1.shape("arrow") 
t2.shape("turtle") 
t1.penup() 
t2.penup() 
t1.color("red") 
t2.color("green") 
t1.goto(-1*width,30) 
t2.goto(-1*width,-30) 

a=input("Введіть черепашку на яку ставите\n 1 abo 2")


def win(t):
    t.goto(-50,80)
    t.write("            I AM WINNER!!!  ", font=("Arial",12,"bold"))
    ##################
    t.right(100)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(145)
    t.forward(60)
    t.right(160)
    t.forward(60)
    t.right(150)
    t.forward(60)
    t.right(115)
    t.forward(10)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    
     
while t1.xcor()<width or t2.xcor()<width:
    t1.forward(randint(2,7)) 
    t2.forward(randint(2,7))
if t1.xcor()>t2.xcor():
    win(t1)
    if a==1:
        print("ВИ ВИГРАЛИ 1000 ГРН")
    else:
        print("ВИ ПРОГРАЛИ 1000 ГРН")
        print("ВКАЖІТЬ НОМЕР КАРТИ")
else:
    win(t2)
    if a==2:
        print("ВИ ВИГРАЛИ 1000 ГРН")
    else:
        print("ВИ ПРОГРАЛИ 1000 ГРН")
        print("ВКАЖІТЬ НОМЕР КАРТИ")
exitonclick()