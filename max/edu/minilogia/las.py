from random import randint
from turtle import Turtle, mainloop, tracer, update

bok = 56
__max_t = 8
__delta = 7


def trojkat(p, _bok):
    p.begin_fill()
    p.color("black", "green")
    for i in range(3):
        p.fd(_bok)
        p.rt(120)
    p.end_fill()


def rab(p):
    p.begin_fill()
    p.color("black", "green")
    for i in range(2):
        p.fd(bok / 3)
        p.lt(120)
        p.fd(bok / 3)
        p.lt(60)
    p.end_fill()


def szesciokat(b, k, p):
    p.begin_fill()
    p.color("black", k)
    for i in range(6):
        p.fd(b)
        p.lt(60)
    p.end_fill()


def tlo(p):
    szesciokat(bok, "yellow", p)


def czesc(p):
    rab(p)
    p.fd(bok / 3)
    szesciokat(bok / 3, "lightgreen", p)


def skocz(p):
    p.hideturtle()
    p.pu()
    p.rt(120)
    p.forward(bok)
    p.lt(120)
    p.pd()


def srodek():
    p = Turtle()
    skocz(p)
    tlo(p)
    for i in range(6):
        czesc(p)
        p.fd(bok / 3 * 2)
        p.lt(60)


def galaz(r):
    n = randint(1, __max_t)
    ilosc = bok
    for i in range(n):
        trojkat(r, ilosc)
        r.pu()
        r.fd(ilosc)
        r.rt(120)
        r.fd(ilosc)
        ilosc -= __delta
        r.rt(60)
        r.fd(ilosc / 2)
        r.lt(180)
        r.pd()


def kwiat():
    tracer(0)
    srodek()
    for i in range(6):
        l = Turtle()
        l.lt(i * 60)
        skocz(l)
        galaz(l)
        print(str(i))
    update()


kwiat()
mainloop()
