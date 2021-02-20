# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.shape("turtle")
# tim.color("red")
#
# # Turtle Makes A Square...
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
#
# # Turtle Makes A Square Using While Loop
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# screen = Screen()
# screen.exitonclick()
#
# #  Module That Need To Be Intalled Before Usage...
# import heroes
# print(heroes.gen())

# Turtle That Draw Dashed Line...
# import turtle as t
# from turtle import Screen
#
# tim = t.Turtle()
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# screen = Screen()
# screen.exitonclick()

# # Drawing Different Shapes
# import turtle as t
# from turtle import Screen
# import random
#
# tim = t.Turtle()
# tim.shape("turtle")
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "lightSeaGreen", "wheat",
#            "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
#
# screen = Screen()
# screen.exitonclick()

# Random Walk Of The Turtle
# import turtle as t
# from turtle import Screen
# import random
#
# tim = t.Turtle()
# tim.shape("turtle")
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r, g, b)
#     return random_colour
#
#
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "lightSeaGreen", "wheat",
# #            "SlateGray", "SeaGreen"]
#
# directions = [0, 90, 180, 270]
#
# tim.pensize(10)
#
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()

# # Spirograph Using Turtle
# import turtle as t
# import random
#
# tim = t.Turtle()
# tim.shape("turtle")
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# tim.speed("fastest")
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + 10)
#
#
# draw_spirograph(10)
#
# tim.circle(100)
#
# screen = t.Screen()
# screen.exitonclick()

# Contemporary Art ==> Random Color Spot Painting Project...
# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
tim.shape("turtle")
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()





