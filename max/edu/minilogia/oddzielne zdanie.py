from turtle import Turtle, mainloop, tracer, update
from math import sqrt


p = Turtle()
szer = 360
kol1 = "black"
kol2 = "blue"
kol3 = "yellow"


def ksztalt(bok):
    p.begin_fill()
    p.color(kol1, kol2)
    przek = sqrt(2)*bok
    p.fd(6*bok)
    p.lt(90)
    p.fd(4*bok)
    p.rt(90)
    p.fd(bok)
    p.lt(90)
    p.fd(bok)
    p.rt(90)
    p.fd(bok)
    p.lt(135)
    p.fd(przek)
    p.lt(45)
    p.fd(3*bok)
    p.rt(45)
    p.fd(przek)
    p.lt(90)
    p.fd(przek)
    p.rt(45)
    p.fd(3*bok)
    p.lt(45)
    p.fd(przek)
    p.lt(135)
    p.fd(bok)
    p.rt(90)
    p.fd(bok)
    p.lt(90)
    p.fd(bok)
    p.rt(90)
    p.fd(bok*4)
    p.lt(90)
    p.end_fill()


def ksztalt2(bok):
    p.begin_fill()
    p.color(kol1, kol3)
    p.fd(bok)
    p.lt(90)
    p.fd(bok*3)
    p.lt(90)
    p.fd(bok)
    p.lt(90)
    p.fd(bok*3)
    p.lt(90)
    p.end_fill()


def ksztalt3(bok):
    p.begin_fill()
    p.color(kol1,kol3)
    przek = sqrt(2) * bok
    p.rt(45)
    p.fd(przek)
    p.lt(45)
    p.fd(bok*2)
    p.lt(45)
    p.fd(przek)
    p.lt(45)
    p.fd(bok)
    p.lt(90)
    p.fd(bok)
    p.rt(90)
    p.fd(bok)
    p.lt(90)
    p.fd(bok*2)
    p.lt(90)
    p.fd(bok)
    p.rt(90)
    p.fd(bok)
    p.lt(90)
    p.fd(bok)
    p.lt(90)
    p.end_fill()


def kwadrat(przek):
    p.begin_fill()
    p.color(kol1, kol3)
    for i in range(4):
        p.fd(przek)
        p.lt(90)
    p.end_fill()


def ksztalt_all(bok):
    ksztalt(bok)
    ksztalt2(bok)
    p.fd(bok)
    p.lt(90)
    p.fd(3*bok)
    p.rt(90)
    ksztalt3(bok)
    p.rt(90)
    p.fd(bok*3)
    p.lt(90)
    p.fd(bok*4)
    ksztalt2(bok)
    p.pu()
    p.lt(90)
    p.fd(bok*6)
    p.lt(90)
    p.fd(bok)
    p.rt(45)
    p.pd()
    kwadrat(bok*sqrt(2))
    p.pu()
    p.lt(135)
    p.fd(bok*6)
    p.lt(90)
    p.fd(bok)
    p.pd()


def pas(n, bok):
    for i in range(n):
        ksztalt_all(bok)


def przejscie1(n, bok):
    p.pu()
    p.bk(n*(5*bok))
    p.lt(90)
    p.fd(bok*6)
    p.rt(90)
    p.fd(bok*2.5)
    p.lt(90)
    p.fd(bok)
    p.rt(90)
    p.pd()


def piramida(n):
    il = n
    bok = szer / (n*5+5)
    p.pu()
    p.bk(szer/2)
    p.rt(90)
    p.fd(7*bok*n/2)
    p.lt(90)
    p.pd()
    for i in range(n):
        pas(il, bok)
        przejscie1(il, bok)
        il -= 1

tracer(0)
piramida(10)
update()
mainloop()
