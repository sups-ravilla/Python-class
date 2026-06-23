import turtle

# Initialize the turtle screen
screen = turtle.Screen()
screen.setup(400, 400)

# Create the turtle and draw a square
t = turtle.Turtle()
t.speed(5)
for _ in range(4):
    t.forward(100)
    t.left(90)

# Keep the window open until closed by the user
turtle.done()
