from turtle import Turtle, width, mainloop, pos, tracer, update



p = Turtle()
bok = 500

def tlo (bok2):
    p.begin_fill()
    p.color("blue", "blue")
    for i in range(4):
        p.fd(bok2)
        p.lt(90)
    p.end_fill()

def entlik(a):
    p.color("yellow")
    for i in range(4):
        p.fd(a)
        p.lt(90)
        p.fd(a*3)
        p.lt(90)
        p.fd(a)
        p.lt(90)


def wzor(a):
    for i in range(4):
        entlik(a)
        p.pu()
        p.fd(a*7)
        p.lt(90)
        p.pd()
    p.pu()
    p.fd(2*a)
    p.lt(90)
    p.fd(2*a)
    p.rt(90)
    p.pd()
    entlik(a)

def pentlik(a, bok2):
    t = p.pos()
    p.width(4)
    tlo(bok2)
    p.fd(a)
    p.lt(90)
    p.fd(a)
    p.rt(90)
    wzor(a)
    p.pu()
    p.goto(t)
    p.pd()

def entpent(n):
    a = bok/(n*9)
    bok2 = bok/n
    p.pu()
    p.rt(90)
    p.fd(bok/2)
    p.rt(90)
    p.fd(bok/2)
    p.lt(180)
    p.pd()
    for i in range(n):
        for m in range(n):
            pentlik(a, bok2)
            p.pu()
            p.fd(bok2)
            p.pd()
        p.pu()
        p.bk(n*bok2)
        p.lt(90)
        p.fd(bok2)
        p.rt(90)
        p.pd()
tracer(0)
entpent(3)
update()
mainloop()