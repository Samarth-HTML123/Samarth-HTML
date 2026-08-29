import turtle


screen = turtle.Screen()
screen.title("Draw a Square")


pen = turtle.Turtle()
pen.speed(2)  

for _ in range(4):
    pen.forward(100)  
screen.exitonclick()
