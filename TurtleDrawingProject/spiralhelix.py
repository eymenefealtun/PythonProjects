import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Python Turtle")

turtle_instace = turtle.Turtle()
turtle_instace.speed(0)

turtle_colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(200):
    turtle_instace.color(turtle_colors[i % len(turtle_colors)])
    turtle_instace.circle(10 * i)
    turtle_instace.circle(-10 * i)
    turtle_instace.left(i)


turtle.done()
#turtle.mainloop()