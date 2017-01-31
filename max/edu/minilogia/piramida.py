from math import sqrt
from turtle import Turtle, mainloop, tracer, update

p = Turtle()


def kwadracik(bok):
    p.begin_fill()
    p.color("black", "red")
    przek1 = bok / 2 * sqrt(2)
    bok1 = int(przek1 / 5)
    przek2 = bok1 * sqrt(2)
    for i in range(4):
        d = int(bok1 * 2)
        p.forward(d)
        p.rt(90)
        p.fd(bok1)
        p.rt(90)
        p.fd(bok1)
        p.lt(135)
        p.fd(przek2)
        p.lt(45)
        p.fd(bok1)
        p.lt(45)
        p.fd(przek2)
        p.lt(135)
        p.fd(bok1)
        p.rt(90)
        p.fd(bok1)
        p.rt(90)
        p.fd(bok1 * 2)
        p.lt(90)
    p.end_fill()


def piramida(n):
    bok2 = 600 / n
    przek1 = bok2 / 2 * sqrt(2) - 5
    ilosc = 5
    p.pu()
    p.bk(600 / 2 + 55)
    p.pd()
    for i in range(n):
        for k in range(ilosc):
            kwadracik(bok2)
            p.pu()
            p.fd(przek1 * 2)
            p.pd()
        p.pu()
        p.bk(ilosc * (przek1 * 2))
        p.fd(przek1)
        p.lt(90)
        p.fd(przek1)
        p.rt(90)
        p.pd()
        ilosc -= 1


tracer(0)
piramida(5)
update()
mainloop()
