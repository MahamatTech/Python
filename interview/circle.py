import turtle
my_turtle = turtle.Turtle()

def square(length, angle):
    my_turtle.forward(length)
    my_turtle.left(angle)

for circle_turtle in range(24):
    for turtle in range(4):
        square(300, 90)
    my_turtle.left(15)