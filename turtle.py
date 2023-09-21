import turtle
t=turtle.Turtle()
ts=t.getscreen()
t.shape("turtle")
t.color("yellow")
ts.bgcolor("black")
def move():
    t.forward(2)
def turn_left():
    t.left(90)
def turn_right():
    t.left(90)
def spin():
    for i in range (4):
     t.right(90)
def exit():
    ts.bye()
ts.onkey(move,"space")
ts.onkey(turn_left,"left")
ts.onkey(turn_right,"right")
ts.onkey(spin,"s")  
ts.onkey(exit,"q") 
