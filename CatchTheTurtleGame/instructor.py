import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Cathc the Turtle")

top_height = screen.window_height() / 2
FONT = ('Arial', 30, 'normal')
turtle_list = []
score = 0
game_over = False
grid_size = 10
time = 20

score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()
    score_turtle.goto(0, top_height * 0.8)
    score_turtle.write("Score: 0", False, "center", FONT)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    countdown_turtle.goto(0, top_height * 0.6)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.write(f"Time: {time}", False, "center", FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(f"Game over", False, "center", FONT)

def make_turtle(x, y, ):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", False, "center", FONT)

    t.onclick(handle_click)
    t.shape('turtle')
    t.penup()
    t.shapesize(2, 2)
    t.color('dark green')
    t.setpos(x * grid_size, y * grid_size)
    t.speed('fastest')
    turtle_list.append(t)
    return t

def setup_Turtles():
    temp = 20
    while temp >= -20:
        for i in range(-20, 21, 10):
            make_turtle(i, temp)
        temp = temp - 10

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        global time
        hide_turtles()
        random.choice(turtle_list).showturtle()  # chooses a element from given list randomly
        time -= 1
        screen.ontimer(show_turtles_randomly, 500)
    else:
        hide_turtles()


turtle.tracer(0)
setup_score_turtle()
setup_Turtles()
hide_turtles()
show_turtles_randomly()
countdown(20)
turtle.tracer(1)

turtle.mainloop()
