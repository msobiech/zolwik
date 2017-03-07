from turtle import Turtle, tracer, update, mainloop, pos

p = Turtle()
kat = (360+180+180)/6

def szesc(bok):
    for i in range(6):
        p.fd(bok)
        p.lt(180-kat)


def rzad(ilosc, bok):
    p.lt(30)
    for i in range(ilosc):
        szesc(bok)
        p.pu()
        p.fd(bok)
        p.rt(180-kat)
        p.fd(bok)
        p.lt(180-kat)
        p.pd()



def piramida(ilosc):
    bok = 499/ilosc/3
    il = ilosc
    for i in range(ilosc):
        bierzaca = p.pos()
        rzad(il, bok)
        il -= 1
        p.pu()
        p.goto(bierzaca)
        p.seth(90)
        p.fd(bok)
        p.rt(180 - kat)
        p.fd(bok)
        p.rt(30)
        p.pd()

piramida(3)
mainloop()