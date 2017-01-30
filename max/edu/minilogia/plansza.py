from turtle import Turtle

__bok__ = 400
__color_1__ = "red"
__color_2__ = "green"
__wypelnienie___ = "black"
p = Turtle()


def tlo():
    p.begin_fill()
    for i in range(4):
        p.fd(400)
        p.lt(90)
    p.end_fill()


def ksztalt(__bok, kolor):
    p.begin_fill()
    p.color(__wypelnienie___, kolor)
    for i in range(2):
        p.fd(__bok)
        p.rt(90)
        p.fd(__bok)
        p.lt(90)
        p.fd(__bok)
        p.lt(90)
        p.fd(__bok)
        p.rt(90)
    for i in range(3):
        p.fd(__bok)
        p.lt(90)
    p.lt(180)
    for i in range(2):
        p.fd(__bok)
        p.lt(90)
        p.fd(__bok)
        p.lt(90)
        p.fd(__bok)
        p.rt(90)
        p.fd(__bok)
        p.rt(90)
    p.lt(180)
    p.fd(__bok)
    p.lt(90)
    p.end_fill()


def ksztalt2(__bok, kolor):
    p.begin_fill()
    p.color(__wypelnienie___, kolor)
    for i in range(2):
        p.fd(__bok)
        p.rt(90)
        p.fd(__bok)
        p.lt(90)
        p.fd(__bok)
        p.lt(90)
        p.fd(__bok)
        p.rt(90)
    p.lt(90)
    p.fd(__bok)
    for i in range(2):
        p.fd(__bok)
        p.lt(90)
        p.fd(__bok)
        p.lt(90)
        p.fd(__bok)
        p.rt(90)
        p.fd(__bok)
        p.rt(90)
    p.lt(180)
    p.fd(__bok)
    p.lt(90)
    p.end_fill()


def czesc(__bok, kolor):
    p.begin_fill()
    p.color(__wypelnienie___, kolor)
    for i in range(4):
        p.fd(__bok)
        p.lt(90)
    p.end_fill()


def pas(n, kolor):
    bok2 = __bok__ / (n * 6)
    czesc(bok2, kolor)
    p.fd(bok2 * 2)
    for i in range(n - 1):
        ksztalt(bok2, kolor)
        p.pu()
        p.fd(6 * bok2)
        p.pd()
    ksztalt2(bok2, kolor)


def przejscie(n):
    bok2 = __bok__ / (n * 6)
    p.pu()
    p.fd(4 * bok2)
    p.lt(90)
    p.fd(4 * bok2)
    p.lt(90)
    p.pd()


def przejscie2(n):
    bok2 = __bok__ / (n * 6)
    p.pu()
    p.fd(4 * bok2)
    p.rt(90)
    p.fd(2 * bok2)
    p.rt(90)
    p.pd()


def pasy(n):

    pas(n, "%s" % __color_1__)
    przejscie(n)
    pas(n, "%s" % __color_2__)
    przejscie2(n)


def plansza(n):
    p.getscreen().tracer(0)
    bok2 = __bok__ / (n * 6)
    p.pu()
    p.rt(90)
    p.fd(__bok__ / 2)
    p.rt(90)
    p.fd(__bok__ / 2)
    p.lt(180)
    p.pd()
    tlo()
    p.lt(90)
    p.fd(bok2)
    p.rt(90)
    for i in range(n):
        pasy(n)
    p.hideturtle()
    p.getscreen().update()


plansza(10)
p.getscreen().mainloop()
