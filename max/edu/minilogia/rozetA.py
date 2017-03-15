from turtle import Turtle, circle, tracer, update, mainloop

p = Turtle()
bok = 500
promien = 250
bok_trojkata = promien/2
def rab(bok1):
    bok = bok_trojkata
    for i in range(2):
        p.fd(bok1)
        p.lt(120)
        p.fd(bok1)
        p.bk(bok1)
        p.rt(60)
        p.fd(bok1)
        p.lt(120)


def gwiazda(bok1):
    for i in range(6):
        rab(bok1)
        p.fd(bok1)
        p.rt(60)
        p.fd(bok1)
        p.lt(120)

def linie():
    p.rt(90)
    for i in range(6):
        p.fd(promien)
        p.bk(promien)
        p.lt(60)

def rozeta():
    linie()
    p.fd(promien)
    p.lt(90)
    p.circle(promien)
    p.lt(60)
    gwiazda(promien/1.73)
    p.lt(30)
    p.fd(bok_trojkata)
    p.rt(30)
    gwiazda(promien/1.73/2)

tracer(0)
rozeta()
update()
mainloop()