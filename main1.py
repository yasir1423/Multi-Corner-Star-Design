from turtle import *
from colorsys import *
bgcolor('black')
tracer(48)
pensize(2)
hideturtle()
h=0.8
for i in range(300):
    color(hsv_to_rgb(h,0.9,1))
    h+=0.002
    forward(i*2)
    left(150)
    dot(25)
done()