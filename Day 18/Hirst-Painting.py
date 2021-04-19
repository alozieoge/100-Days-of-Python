# Part 1
# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
# for color in colors:
#     # rgb = color.rgb[0], color.rgb[1], color.rgb[2]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
#
# color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
# (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
# (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
# (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


# Part 2
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.setposition(-200, -200)
tim.speed("fastest")

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

rows = 10
columns = 10
spacing = 50
default_x = tim.xcor()


# def reset_x_position():
#     tim.left(90)
#     tim.forward(spacing)
#     tim.setposition(default_x, tim.ycor() + spacing)
#     tim.right(90)
#     tim.setx(position[0])


for row in range(rows):
    for column in range(columns):
        tim.dot(20, random.choice(color_list))
        if column < columns - 1:
            tim.forward(spacing)
    if row < rows - 1:
        # reset_x_position()
        tim.setheading(0)
        tim.setposition(default_x, tim.ycor() + spacing)


screen = t.Screen()
screen.exitonclick()
