import turtle

drawing_board = turtle.Screen()

drawing_board.bgcolor("green")

drawing_board.title("Python turtle")

turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(50)

    turtle_instance.left(90)

turtle.done()
