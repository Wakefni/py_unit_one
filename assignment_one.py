# Nicholas Wakefield
# 9/21/23
#This program draws 4 octogons
import turtle
turtle.penup()
turtle.goto(100,100)
def drawOctogon(mycolor):
    turtle.color(mycolor)
    turtle.begin_fill()
    for x in range (8):
        turtle.forward(50)
        turtle.left(45)
    turtle.end_fill()
turtle.pendown()
drawOctogon("pink")
def runMan(coords1, coords2):
    turtle.penup()
    turtle.goto(coords1, coords2)
    turtle.pendown()
runMan(-100, 100)
drawOctogon("magenta")
runMan(-100, -100)
drawOctogon("red")
runMan(100, -100)
drawOctogon("blue")
turtle.exitonclick()
