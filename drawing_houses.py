#Nicholas Wakefield
#9/22/23
#This program draws a house with three variables, size, house color and roof color
import turtle
def movePen(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.right(60)
    turtle.pendown()
def drawHouse(size, house_color, roof_color):
    turtle.color(house_color)
    turtle.fillcolor(house_color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(size)
    turtle.color(roof_color)
    turtle.begin_fill()
    turtle.right(30)
    for x in range(3):
        turtle.forward(size)
        turtle.right(120)
    turtle.end_fill()
drawHouse(100, "pink", "brown")
movePen(-100, 100)
drawHouse(50, "blue", "purple")
movePen(-100, -100)
drawHouse(75, "red", "black")
movePen(100, -100)
drawHouse(25, "green", "yellow")

turtle.exitonclick()