from turtle import Turtle, mainloop, tracer, update
from math import sqrt


p = Turtle()
kolor = "lime"


def element1(bok,y):
    y.begin_fill()
    y.color("black", kolor)
    przek = bok*sqrt(2)
    y.rt(45)
    y.fd(przek * 2)
    y.lt(90)
    y.fd(przek)
    y.lt(45)
    y.fd(bok * 2)
    y.lt(45)
    y.fd(przek)
    y.lt(90)
    y.fd(przek * 2)
    y.lt(135)
    y.end_fill()


def element2(bok, r):
    r.seth(0)
    r.lt(180)
    element1(bok, r)
    r.lt(180)
    element1(bok, r)


def element3(bok):
    przek = bok*sqrt(2)
    element2(bok, p)
    t = p.clone()
    p.lt(45)
    t.rt(45)
    p.fd(przek)
    t.fd(przek)
    p.fd(przek)
    t.fd(przek)
    p.rt(90)
    t.lt(90)
    p.fd(przek)
    t.fd(przek)
    p.lt(90)
    t.rt(90)
    p.fd(przek)
    t.fd(przek)
    p.fd(przek)
    t.fd(przek)
    element2(bok, p)
    element2(bok, t)
    t.lt(45)
    p.rt(45)
    t.fd(przek)
    p.fd(przek)
    t.fd(przek)
    p.fd(przek)
    t.rt(90)
    p.lt(90)
    t.fd(przek)
    p.fd(przek)
    t.lt(90)
    p.rt(90)
    t.fd(przek)
    p.fd(przek)
    t.fd(przek)
    p.fd(przek)
    element2(bok, p)
    t.rt(45)


def pas(n):
    szer = 700
    p.seth(0)

    bok = szer/(n*10+6)
    p.pu()
    p.bk((szer/2)-(3*bok))
    p.pd()
    for i in range(n):
        element3(bok)

pas(13)
mainloop()
