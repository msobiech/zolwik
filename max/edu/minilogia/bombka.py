from turtle import Turtle, mainloop, tracer, update, circle

p = Turtle()
kolor_bombki = "blue"
kolor_gwiazki = "gold"
#http://logia.oeiizk.waw.pl/
#15:45

def wysrodkowanie(r):
    p.rt(90)
    p.pu()
    p.fd(r)
    p.seth(0)


def tlo(r):
    p.begin_fill()
    p.color(kolor_bombki, kolor_bombki)
    p.circle(r)
    p.end_fill()


def gwiazdka(r):
    p.begin_fill()
    p.color(kolor_bombki, kolor_gwiazki)
    for i in range(5):
        p.fd(r*2-10)
        p.rt(180 - 36)
    p.end_fill()


def bombka(r):
    wysrodkowanie(r)
    tlo(r)
    p.lt(90)
    p.fd(r*2)
    p.rt(180 - (36/2))
    gwiazdka(r)

tracer(0)
bombka(100)
update()
mainloop()