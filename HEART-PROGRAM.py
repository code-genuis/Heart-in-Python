from turtle import *
import time

def draw_shape():
    bgcolor('yellow')
    color('red')
    begin_fill()
    pensize(3)
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    end_fill()

time_limit = 5

start_time = time.time()
while time.time() - start_time < time_limit:
    draw_shape()
    break 

done()
