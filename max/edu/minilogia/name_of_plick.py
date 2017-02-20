from turtle import Turtle, mainloop, tracer, update

bok = 510
bok2 = int(bok / 34)
p = Turtle()


def romb():
    p.begin_fill()
    p.color("green", "green")
    for i in range(2):
        p.forward(bok2)
        p.lt(120)
        p.fd(bok2)
        p.lt(60)
        p.fd(bok2)
        p.lt(120)
        p.fd(bok2)
        p.lt(60)
    p.end_fill()


def _bok():
    romb()
    p.fd(bok2 * 2)
    p.lt(60)
    p.fd(bok2)
    p.lt(120)
    p.fd(bok2)
    p.lt(60)
    romb()
    p.fd(bok2)
    p.lt(120)
    p.fd(bok2)


def czesc1():
    for i in range(6):
        _bok()
        p.lt(60)


def _bok2(n):
    for i in range(n):
        czesc1()
        p.pu()
        p.fd(bok2 * 3)
        p.pd()
    p.pu()
    p.bk(bok2)
    p.pd()


def obwod(n):
    for i in range(6):
        _bok2(n)
        p.lt(60)


def przejscie():
    p.fd(bok2 * 2)
    p.lt(60)
    p.fd(bok2 * 2)
    p.lt(60)
    p.fd(bok2)
    p.lt(60)
    p.fd(bok2)
    p.lt(180)


def posadzka():
    p.pu()
    p.rt(90)
    p.fd(bok/3)
    p.rt(90)
    p.fd(bok/3)
    p.lt(180)
    p.pd()
    tracer(0)
    il = int(6)
    for i in range(5):
        obwod(il)
        przejscie()
        il -= 1
    update()

tracer(0)
posadzka()
update()
mainloop()

