from math import sqrt
from turtle import Turtle, mainloop, tracer, update

p = Turtle()
kolor = "blue"
kolor2 = "white"


def kwadracik(bok):
    p.begin_fill()
    p.color(kolor, kolor)
    for i in range(4):
        p.fd(bok)
        p.lt(90)
    p.end_fill()


def przek(bok):
    kwadracik(bok)
    p.begin_fill()
    p.color(kolor2, kolor2)
    p.lt(90)
    p.fd(bok)
    p.rt(90)
    p.fd(bok)
    p.rt(135)
    p.fd(sqrt(2) * bok)
    p.lt(135)
    p.end_fill()


def element(bok):
    for i in range(4):
        kwadracik(bok)
        p.fd(bok)
        przek(bok)
        p.pu()
        p.fd(bok * 2)
        p.rt(90)
        p.fd(bok)
        p.lt(180)
        p.pd()


def koronka(n):
    bok = 760 / (n * 3 + 1)
    p.pu()
    p.bk(760 / 2)
    p.pd()
    for i in range(n):
        element(bok)
        p.pu()
        p.fd(bok * 3)
        p.pd()


tracer(0)
koronka(4)
update()
mainloop()
