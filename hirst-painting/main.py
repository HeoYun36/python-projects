# import colorgram
# colors = colorgram.extract("image.jpg", 30)
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_list.append((r, g, b))
#
# print(colors_list)
import turtle as t
import random

color_list = [(142, 77, 52), (188, 165, 118), (165, 152, 38), (16, 46, 83), (46, 110, 135), (144, 57, 83),
              (61, 120, 100), (143, 184, 174), (141, 170, 176), (86, 36, 30), (65, 152, 168), (219, 209, 96),
              (109, 38, 32), (102, 145, 110), (166, 98, 130), (95, 122, 169), (161, 140, 160), (176, 104, 84),
              (52, 52, 87), (206, 182, 195), (67, 47, 63), (75, 51, 67), (174, 200, 193), (171, 200, 203),
              (217, 180, 172), (182, 191, 206)]

tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed("fast")


def hirst_paint(x, y):
    tim.setx(-250)
    tim.sety(-250)
    first_x_position = tim.xcor()
    first_y_position = tim.ycor()
    for j in range(y):
        for i in range(x):
            tim.color(random.choice(color_list))
            tim.dot(20)
            tim.forward(50)
        tim.setposition(first_x_position, first_y_position + 50)
        first_y_position += 50


hirst_paint(10, 10)

screen = t.Screen()
screen.exitonclick()
