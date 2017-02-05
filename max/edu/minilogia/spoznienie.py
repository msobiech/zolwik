from math import sqrt
from turtle import Turtle, mainloop, tracer, update

# http://minilogia.oeiizk.waw.pl/archiwum/zadania/3etap07.pdf

bok = 500 / 12
p = Turtle()


def pentagon(r):
    for i in range(5):
        r.fd(bok)
        r.rt(72)


def element(y):
    y.pd()
    for i in range(5):
        pentagon(y)
        y.fd(bok)
        y.lt(72)
    y.pu()


def przejscie2():
    p.fd(bok)
    p.lt(72)
    p.fd(bok)
    p.rt(36)
    p.fd(bok)
    p.rt(36)
    p.fd(bok)
    p.rt(36)
    p.fd(bok)
    p.lt(72)


def przejscie3(t):
    t.fd(bok)
    t.rt(72)
    t.fd(bok)
    t.lt(36)
    t.fd(bok)
    t.lt(36)
    t.fd(bok)
    t.rt(72)


def element2():
    p.pd()
    element(p)
    t = p.clone()
    przejscie2()
    element(p)
    t.lt(108)
    przejscie3(t)
    t.pd()
    element(t)
    t.pu()
    t.hideturtle()


def przejscie(promien):
    p.fd(promien)
    p.lt(36 / 2)
    p.fd(bok)
    p.rt(36)
    p.fd(bok)
    p.rt(36)


def wzor():
    promien = bok * sqrt(50 + 10 * sqrt(5)) / 10
    # rysuje srodek
    p.pu()
    p.lt(360 - 234)
    p.fd(promien)
    p.seth(0)
    element(p)
    p.lt(54)
    p.fd(promien)
    p.seth(90)
    for i in range(5):
        bierzaca = p.pos()
        poz = p.heading()
        przejscie(promien)
        element2()
        p.goto(bierzaca)
        p.seth(poz)
        p.lt(72)
    p.hideturtle()


tracer(0)
wzor()
update()
mainloop()
