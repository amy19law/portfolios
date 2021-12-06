import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("French Flag")

frenchFlag = turtle.Turtle()

x = -200
y = 200

for flagColours in ["blue", "white", "red"]:
    frenchFlag.color(flagColours)
    frenchFlag.penup()
    frenchFlag.goto(x,y)
    frenchFlag.pendown()
    frenchFlag.begin_fill()
    for side in range(0,2):
        frenchFlag.forward(100)
        frenchFlag.left(-90)
        frenchFlag.forward(200)
        frenchFlag.left(-90)
    frenchFlag.end_fill()
    x = frenchFlag.xcor() + 100

frenchFlag.hideturtle()

#def blue ():
#    frenchFlag.color("blue")
#    frenchFlag.penup()
#    frenchFlag.goto(-200,200)
#    frenchFlag.pendown()
#    frenchFlag.begin_fill()
#    frenchFlag.forward(100)
#    frenchFlag.left(-90)
#    frenchFlag.forward(200)
#    frenchFlag.left(-90)
#    frenchFlag.forward(100)
#    frenchFlag.left(-90)
#    frenchFlag.forward(200)
#    frenchFlag.left(-90)
#    frenchFlag.end_fill()

#def white ():
#    frenchFlag.color("white")
#    frenchFlag.penup()
#    frenchFlag.goto(-100,200)
#    frenchFlag.pendown()
#   frenchFlag.begin_fill()
#    frenchFlag.forward(100)
#    frenchFlag.left(-90)
#    frenchFlag.forward(200)
#    frenchFlag.left(-90)
#    frenchFlag.forward(100)
#    frenchFlag.left(-90)
#    frenchFlag.forward(200)
#    frenchFlag.left(-90)
#    frenchFlag.end_fill()

#def red ():
#    frenchFlag.color("red")
#    frenchFlag.penup()
#    frenchFlag.goto(0,200)
#    frenchFlag.pendown()
#    frenchFlag.begin_fill()
#    frenchFlag.forward(100)
#    frenchFlag.left(-90)
#    frenchFlag.forward(200)
#    frenchFlag.left(-90)
#    frenchFlag.forward(100)
#    frenchFlag.left(-90)
#    frenchFlag.forward(200)
#    frenchFlag.left(-90)
#    frenchFlag.end_fill()

#frenchFlag.hideturtle()

#blue()
#white()
#red()
