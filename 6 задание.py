from turtle import *

tracer(0) ## выкл анимации передвижения
r = 50

for i in range(7):
    rt(90)
    fd(4*r)
    for k in range(2):
        lt(90)
        fd(4*r)

up() ## поднятие хвоста

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*r,y*r)
        dot(3,'blue')

update()
exitonclick()