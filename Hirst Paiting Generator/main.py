import colorgram
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_colors)

def draw_hirst(grid_size, dot_size=20, spacing=50):
    start_x = -grid_size * spacing // 2  # Shift left to start from the bottom-left
    start_y = -grid_size * spacing // 2  # Shift down to start from the bottom-lef

    for row in range(grid_size):
        for col in range(grid_size):
            tim.goto(start_x + col * spacing, start_y + row * spacing)
            tim.dot(dot_size, random.choice(rgb_colors))


draw_hirst(10)

screen = turtle.Screen()
screen.exitonclick()