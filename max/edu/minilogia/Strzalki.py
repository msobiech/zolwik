from math import sqrt
from turtle import Turtle, mainloop, tracer, update

p = Turtle()
szerokosc = 500


def strzalka(bok, kolor):
    sqrt_bok = sqrt(2) * bok
    bok2 = bok / 2
    p.begin_fill()
    p.color("black", kolor)
    p.fd(bok)
    p.lt(90)
    p.fd(bok2)
    p.rt(90)
    p.fd(bok)
    p.rt(90)
    p.fd(bok2)
    p.lt(90)
    p.fd(bok)
    p.rt(90)
    p.fd(bok)
    p.rt(90)
    p.fd(bok2)
    p.lt(45)

    p.fd(sqrt_bok)
    p.rt(90)
    p.fd(sqrt_bok)
    p.lt(45)
    p.fd(bok2)
    p.rt(90)
    p.fd(bok)
    p.rt(90)
    p.end_fill()


def wzorek(bok):
    strzalka(bok, "green")
    p.pu()
    p.fd(bok * 2.5)
    p.lt(90)
    p.fd(bok)
    p.rt(90)
    p.pd()
    strzalka(bok, "red")
    p.pu()
    p.fd(bok * 2.5)
    p.rt(90)
    p.fd(bok)
    p.lt(90)
    p.pd()
    strzalka(bok, "green")


'''
for i in range(2):
    kawal(10)
'''


def szer():
    p.pu()
    p.rt(90)
    p.fd(50)
    p.lt(90)
    p.fd(szerokosc / 2)
    p.rt(180)
    p.pd()
    p.fd(szerokosc)
    p.pu()
    p.home()


def strzalki(n):
    tracer(0)
    il = n
    bok = szerokosc / (n * 3 + (n - 1) * 2 + 5)
    n * 3.5
    p.pu()
    p.bk(szerokosc / 2)
    p.rt(90)
    w = int(((3.5 * n) * bok) / 2) - (2 * bok)
    p.fd(w)
    p.lt(90)
    p.pd()
    for i in range(n):
        bierzaca = p.pos()
        for n in range(il):
            wzorek(bok)
        p.pu()
        p.goto(bierzaca)
        p.fd(bok * 2.5)
        p.lt(90)
        p.fd(bok * 3.5)
        p.rt(90)
        p.pd()
        il -= 1
    update()


strzalki(4)
mainloop()
