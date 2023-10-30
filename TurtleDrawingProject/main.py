import math
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#f1f1f1")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()


# square
def CreateSquareWithWhileLoop(turtle_instance):
    i = 0;
    while i < 4:
        turtle_instance.forward(100)
        turtle_instance.right(90)
        i = i + 1


def CreateSquareWithForLoop(turtle_instance):
    for i in range(4):
        turtle_instance.forward(100)
        turtle_instance.right(90)


# star
def CreateStar(turtle_instance):
    turtle_instance.left(108)
    turtle_instance.forward(100)
    turtle_instance.left(144)
    turtle_instance.forward(100)
    for i in range(4):
        turtle_instance.right(72)
        turtle_instance.forward(100)
        turtle_instance.left(144)
        turtle_instance.forward(100)


# sub sqaures
def CreateShrinkSquare(turtle_instance):
    turtle_instance.color("blue")
    sizeOfTheSquare = 30;
    while (sizeOfTheSquare < 100):
        for i in range(4):
            turtle_instance.left(90)
            turtle_instance.forward(sizeOfTheSquare)
        sizeOfTheSquare = sizeOfTheSquare + 10;


CreateShrinkSquare(turtle_instance)
turtle.done();
