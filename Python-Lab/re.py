import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
flower = turtle.Turtle()
flower.speed(0)  # Fastest drawing
flower.width(2)

# Color configuration
num_colors = 36
hue = 0

# Draw flower
for i in range(360):
    # Use HSV to RGB for smooth color transition
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    flower.color(color)
    flower.forward(100)
    flower.left(45)
    flower.forward(50)
    flower.left(90)
    flower.forward(50)
    flower.left(45)
    flower.forward(100)
    flower.right(100)

    hue += 1/num_colors  # Slight hue change per iteration

# Hide turtle and finish
flower.hideturtle()
turtle.done()
