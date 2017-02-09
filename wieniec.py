from turtle import Turtle, mainloop, tracer, update


bok = 25
kat = 36
p = Turtle()
kolor1 = "purple"
kolor2 = "yellow"
#20:50


def romb(kolor):
    p.begin_fill()
    p.color("black", kolor)
    for i in range(2):
        p.fd(bok)
        p.lt(180 - (180 - kat))
        p.fd(bok)
        p.lt(180 - kat)
    p.end_fill()


def kwiat():
    for i in range(5):
        romb(kolor1)
        p.lt(kat)
        romb(kolor2)
        p.lt(36)


def wieniec(n):
    if n == 1:
        for i in range(10):
            kwiat()
            p.fd(bok)
            p.lt(kat)
            p.fd(bok*2)
            p.rt(kat)
            p.fd(bok)
            p.lt(kat)
    if n == 2:
        for i in range(10):
            kwiat()
            p.rt(kat)
            p.fd(bok)
            p.rt(kat)
            p.fd(bok*2)
            p.lt(kat)
            p.fd(bok)


def wianek():
    p.rt(kat/2)
    p.fd(bok)
    p.lt(kat)
    p.fd(bok)
    p.seth(270)
    wieniec(1)
    p.pu()
    p.home()
    p.pd()
    p.seth(180-kat/2)
    p.fd(bok)
    p.lt(kat)
    p.fd(bok)
    p.seth(90)
    p.lt(kat+180)
    wieniec(2)

tracer(0)
wianek()
update()
mainloop()