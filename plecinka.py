from math import sqrt
from turtle import Turtle, mainloop, tracer, update

p = Turtle()

abok = 799


def tlo(bok, kolor):
    p.begin_fill()
    p.color(kolor)
    for i in range(4):
        p.fd(bok)
        p.lt(90)
    p.end_fill()


def przepaska(kolor, bok):
    bok2 = bok / 3
    bok3 = bok2 / sqrt(2)
    bok2 = bok2 / 2
    p.begin_fill()
    p.color(kolor, kolor)
    for i in range(2):
        p.fd(bok2)
        p.lt(45)
        p.fd(5 * bok3)
        p.lt(45)
        p.fd(bok2)
        p.lt(90)
    p.end_fill()


def bialas(bok):
    bak2 = bok / sqrt(2)
    p.begin_fill()
    p.color("white")
    for i in range(4):
        p.fd(bak2)
        p.lt(90)
    p.end_fill()


def krzyz(bok, kolor1, kolor2):
    tlo(bok, kolor2)
    p.fd(bok / 2)
    p.lt(45)
    bialas(bok)
    p.pu()
    p.rt(45)
    p.bk(bok / 2)
    for i in range(2):
        przepaska(kolor1, bok)
        p.pu()
        p.fd(bok)
        p.lt(90)

        przepaska(kolor2, bok)
        p.pu()
        p.fd(bok)
        p.lt(90)



def pas(bok, kolor):
    bok2 = bok / 3
    bok3 = bok2 / sqrt(2)
    p.begin_fill()
    p.color(kolor)
    p.fd(bok2)
    p.lt(45)
    p.fd(bok3)
    p.lt(45)
    p.fd(bok2)
    p.lt(135)
    p.fd(bok3 * 3)
    p.lt(135)
    p.end_fill()


def wariant1(bok):
    krzyz(bok, "black", "gray")
    for i in range(2):
        p.fd(bok / 2)
        pas(bok, 'black')
        p.fd(bok / 2)
        p.lt(90)
        p.fd(bok)
        p.lt(90)


def wariant2(bok):
    krzyz(bok, "gray", "black")
    for i in range(2):
        p.pu()
        p.fd(bok / 2)
        pas(bok, 'gray')
        p.fd(bok / 2)
        p.lt(90)
        p.fd(bok)
        p.lt(90)


def pas2(ilosc):
    p.pu()
    p.bk(abok/2)
    il = 1
    bok2 = abok / ilosc
    for i in range(ilosc):
        if il % 2 == 0:
            wariant2(bok2)
        else:
            wariant1(bok2)
        p.fd(bok2)
        il += 1


tracer(0)
pas2(4)
update()
mainloop()
