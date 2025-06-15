
# import colorgram

# colors = colorgram.extract('image.jpg',30)

# for color in colors:
#     print(color.rgb)   #its a one way 


# rgb_colors = []

# for color in colors:
#     actions_tuple = (color.rgb.r,color.rgb.g,color.rgb.b) 
#     rgb_colors.append(actions_tuple)

#     #   below line one give us the all Rgb color rest 3 line is for separetly retrive the r , g and b color for each portion...
#     # rgb_colors.append(color.rgb)
#     # rgb_colors.append(color.rgb.r)
#     # rgb_colors.append(color.rgb.g)
#     # rgb_colors.append(color.rgb.b)

# print(rgb_colors)

import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

color_list = [(252, 251, 248), (219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150), (247, 251, 248), (41, 46, 65), 
(162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (238, 241, 245), (81, 133, 107), (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58), (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207), (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180), (210, 184, 180), (41, 73, 82)]

def x_wise():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

def left_wise():
    timmy.left(90)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    timmy.left(90)

def right_wise():
    timmy.right(90)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    timmy.right(90)


for _ in range(10):
    x_wise()
    left_wise()
    x_wise()
    right_wise()

    



screen = t.Screen()
screen.exitonclick()
