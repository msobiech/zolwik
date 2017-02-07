from turtle import Turtle, tracer, update, mainloop
from math import sqrt


#19:32
p = Turtle()
szer = 760


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


def trojkat(bok, kolor):
    bok2 = bok*sqrt(2)
    p.begin_fill()
    p.color(kolor, kolor)
    p.fd(bok)
    p.lt(135)
    p.fd(bok2)
    p.lt(135)
    p.fd(bok)
    p.lt(90)
    p.end_fill()


def tlo(bok):
    p.pu()
    bierzaca = p.pos()
    bok2 = bok/(2+sqrt(2)*2)
    kwadrat(bok, "blue")
    for i in range(4):
        rysun_pomoc(bok2)
        p.fd(bok)
        p.lt(90)
    p.lt(45)
    p.fd(bok2)
    p.rt(45)
    for t in range(4):
        trojkat(bok2, "yellow")
        p.fd(bok2*2+(bok2*sqrt(2)))
        p.lt(90)
    p.lt(90)
    p.fd(bok2)
    p.rt(135)
    p.fd(bok2+bok2*sqrt(2))
    p.lt(90)
    trojkat(bok2+bok2*sqrt(2), "red")
    p.lt(90)
    p.fd(bok2+bok2*sqrt(2))
    p.lt(180)
    p.lt(135)
    p.fd(sqrt(2)*bok2)
    p.rt(90)
    p.fd(bok2*2+(bok2*sqrt(2)))
    p.lt(135)
    p.fd(bok2 + bok2 * sqrt(2))
    p.lt(90)
    trojkat(bok2 + bok2 * sqrt(2), "red")
    p.lt(90)
    p.fd(bok2 + bok2 * sqrt(2))
    p.lt(180)
    p.lt(45)
    p.fd(bok2)
    p.rt(45)
    p.bk(bok2)
    kwadrat(bok2*2, "orange")
    p.fd(bok2)
    p.lt(45)
    kwadrat(bok2*sqrt(2), "green")
    p.goto(bierzaca)
    p.seth(0)
    p.pd()


def pas(n):
    bok =szer/n
    p.pu()
    p.bk(szer/2)
    p.rt(90)
    p.fd(bok/2)
    p.lt(90)
    p.pd()
    for n in range(n):
        tlo(bok)
        p.fd(bok)
tracer(0)
pas(3)
update()
mainloop()