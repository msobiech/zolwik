from turtle import Turtle, tracer, update, mainloop
from math import sqrt


#19:32
p = Turtle()


def kwadrat(bok, kolor):
    p.begin_fill()
    p.color(kolor, kolor)
    for i in range(4):
        p.fd(bok)
        p.lt(90)
    p.end_fill()


def rysun_pomoc(bok):
    p.begin_fill()
    p.color("green", "green")
    p.fd(bok)
    p.lt(45)
    p.fd(bok)
    p.lt(135)
    p.fd(bok)
    p.rt(90)
    p.fd(bok)
    p.lt(135)
    p.fd(bok)
    p.lt(45)
    p.fd(bok)
    p.lt(90)
    p.end_fill()


def tlo(bok):
    bok = (bok2*2)+(bok2*sqrt(2)*2)
    bok2 = bok
    kwadrat(100, "red")


def trojkat(bok, kolor)
    bok2 = bok/sqrt(2)
    p.begin_fill()
    p.color(kolor, kolor)
    p.fd(bok)
    p.lt(135)
    p.fd(bok2)
    p.lt(90)
    p.fd(bok2)
    p.lt(135)
    p.end_fill()