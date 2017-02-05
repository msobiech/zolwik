from math import sqrt
from turtle import Turtle, mainloop, tracer, update

bok = 25


def kwadrat(pen, a):
    tracer(130, 90)
    pen.rt(45)
    for i in range(4):
        pen.fd(a)
        pen.lt(90)
    pen.lt(45)
    update()


def wezelek(pen, n, a):
    przek = sqrt(2) * a
    for i in range(n):
        kwadrat(pen, a)
        pen.pu()
        pen.fd(przek / 2)
        pen.pd()


def palka(p, n):
    przek = sqrt(2) * bok
    ilosc = 1
    for i in range(n):
        p.fd(przek)
        wezelek(p, ilosc, bok)
        p.penup()
        p.forward(przek / 2)
        p.pendown()
        ilosc += 1


def peczek(n, y):
    kat = 360 / y
    for i in range(y):
        p = Turtle()
        p.color("red")
        p.hideturtle()
        p.lt(90 + i * kat)
        palka(p, n)


peczek(3, 6)
mainloop()
