from math import *
from turtle import *

# 17:00
kw = 10


def trojkat():
    begin_fill()
    color("green", "green")
    fd(kw * 3)
    lt(135)
    fd(sqrt(2) * (kw * 3))
    lt(135)
    fd(kw * 3)
    lt(90)
    end_fill()


def ksztalt():
    begin_fill()
    color("green", "green")
    fd(3 * kw)
    lt(135)
    fd((kw*sqrt(2)*3))
    rt(45)
    fd(kw)
    lt(90)
    fd(kw)
    rt(45)
    fd(3*(kw*sqrt(2)))
    lt(135)
    fd(3 * kw)
    lt(45)
    fd(kw * 4 * sqrt(2))
    lt(45)
    end_fill()


def kafel():

    for i in range(2):
        trojkat()
        pu()
        fd(4 * kw)
        pd()
        ksztalt()
        pu()
        bk(kw * 4)
        fd(8 * kw)
        lt(90)
        fd(kw * 8)
        lt(91)
        pd()


def kafel2():
    pu()
    lt(90)
    fd(8 * kw)
    lt(180)
    pd()
    kafel()
    pu()
    fd(8 * kw)
    lt(90)
    pd()


def wiersz(n):
    for i in range (n):
        if (i%2==0):
            kafel2()
        else:
            kafel()
        pu()
        fd(kw * 8)
        pd()


def dywan(szer,wys):
    for i in range(wys):
        wiersz(szer)
        if(i % 2 == 0):
            lt(180)
        else:
            lt(90)
            pu()
            fd(kw*16)
            lt(90)

tracer(0)
dywan(4,3)
update()
done()