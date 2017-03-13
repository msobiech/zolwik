from turtle import Turtle, width, mainloop


a = 500/9
p = Turtle()
bok = 500

def tlo ():
    p.begin_fill()
    p.color("blue", "blue")
    for i in range(4):
        p.fd(bok)
        p.lt(90)
    p.end_fill()

def entlik():
    p.color("yellow")
    for i in range(4):
        p.fd(a)
        p.lt(90)
        p.fd(a*3)
        p.lt(90)
        p.fd(a)
        p.lt(90)


def wzor():
    for i in range(4):
        entlik()
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
    entlik()

def pentlik():
    p.rt(90)
    p.fd(bok/2)
    p.rt(90)
    p.fd(bok/2)
    p.lt(180)
    p.width(4)
    tlo()
    p.fd(a)
    p.lt(90)
    p.fd(a)
    p.rt(90)
    wzor()


pentlik()
mainloop()
