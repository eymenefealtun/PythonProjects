import turtle

drawingBoard = turtle.Screen()
drawingBoard.title("A fancy turtle project")
drawingBoard.bgcolor("indian red")

turtleInstance = turtle.Turtle()




def goForward():
    turtleInstance.forward(10)
def rotate_left():
    turtleInstance.setheading(turtleInstance.heading() - 10)
def rotate_right():
    turtleInstance.setheading(turtleInstance.heading()+10)
def clearScreen():
    turtleInstance.clear()
def returnHome():
    penUp()
    turtleInstance.home()
    penDown()
def penUp():
 turtleInstance.penup()

def penDown():
    turtleInstance.pendown()

drawingBoard.listen()
# drawingBoard.onkey(fun=lambda: turtleInstance.forward(100), key="Up" )
drawingBoard.onkeypress(fun=goForward, key="space")
drawingBoard.onkeypress(fun=rotate_right, key="Left")
drawingBoard.onkeypress(fun=rotate_left, key="Right")
drawingBoard.onkey(fun=clearScreen, key="Escape")
drawingBoard.onkey(fun=returnHome, key="Tab")

turtle.done()
