from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clock():
    tim.left(15)

def move_clock():
    tim.right(15)

def reset():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
