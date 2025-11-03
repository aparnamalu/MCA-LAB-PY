import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Flower Drawing")

# Create turtle
flower = turtle.Turtle()
flower.speed(0)  # Fastest speed
flower.width(2)

# Define colors
num_petals = 36
hue = 0

# Draw the flower using HSV color gradient
for i in range(num_petals):
    # Convert HSV to RGB and set color
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    flower.color(r, g, b)
    
    # Begin drawing one petal
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)
    
    flower.left(360 / num_petals)  # Rotate to draw the next petal
    hue += 1 / num_petals

# Hide turtle and finish
flower.hideturtle()
turtle.done()
