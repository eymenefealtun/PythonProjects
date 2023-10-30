import random
import turtle, asyncio, time
from random import randint


def createTurtle(shape, color, speed, isPenUp, hide, shapeSize=1):
    tempTurtle = turtle.Turtle(shape=shape)
    if (isPenUp == True):
        tempTurtle.penup()
    if (hide == True):
        tempTurtle.hideturtle()
    tempTurtle.shapesize(shapeSize)
    tempTurtle.color(color)
    tempTurtle.speed(speed)
    return tempTurtle


mainScreen = turtle.Screen()


def handleScreen():
    global mainScreen
    mainScreen.bgcolor("indian red")
    mainScreen.title("Catch the Turtle")
    mainScreen.screensize(600, 600)


handleScreen()

TURTLE_SIZE = 20
targetTurtleSize = 30
score = 0
time = 20
isStarted = False

targetTurtle = createTurtle("turtle", "green", "fastest", True, False, 2)
scoreTurtle = createTurtle("turtle", "blue", "fastest", True, True)
timerTurtle = createTurtle("turtle", "black", "fastest", True, True)


def setScore(x, y):
    global score
    global isStarted
    if (isStarted == True):
        score = score + 1
    scoreTurtle.clear()
    scoreTurtle.setpos(0, mainScreen.window_height() / 2 - TURTLE_SIZE - 20)
    scoreTurtle.write(f"Score: {score}", 'false', 'center', font=("Verdana", 15, "bold"))


def setInitialScore():
    global score
    scoreTurtle.clear()
    scoreTurtle.setpos(0, mainScreen.window_height() / 2 - TURTLE_SIZE - 20)
    scoreTurtle.write(f"Score: {score}", 'false', 'center', font=("Verdana", 15, "bold"))


def getRandomSign():
    temp = 0
    if (randint(0, 9) < 5):
        return -1
    else:
        return 1


async def setTime(isFinished=False):
    timerTurtle.clear()
    timerTurtle.setpos(0, mainScreen.window_height() / 2 - TURTLE_SIZE - 50)
    if (isFinished == True):
        timerTurtle.write(f"Game Over", 'false', 'center', font=("Verdana", 15, "bold"))
    else:
        global time
        timerTurtle.write(f"Time: {time}", 'false', 'center', font=("Verdana", 15, "bold"))
        targetTurtle.hideturtle()
        targetTurtle.setpos(random.randint(0, 300 - targetTurtleSize) * getRandomSign(),
                            random.randint(0, 300 - targetTurtleSize) * getRandomSign())
        targetTurtle.showturtle()


setInitialScore()
asyncio.run(setTime())


def startGame(x, y):
    global isStarted
    if (isStarted == False):
        isStarted = True
        targetTurtle.showturtle()
        countDown()


mainScreen.listen()
mainScreen.onclick(fun=startGame)

targetTurtle.onclick(fun=setScore)


# targetTurtle.onclick(fun=asyncio.run(setScore()))


def countDown():
    global time
    global isStarted

    def getRandomSign():
        temp = 0
        if (randint(0, 9) < 5):
            return -1
        else:
            return 1

    while time > 0:
        mainScreen.ontimer(asyncio.run(setTime()), 800)
        time = time - 1
    isStarted = False
    asyncio.run(setTime(True))


mainScreen.mainloop()
