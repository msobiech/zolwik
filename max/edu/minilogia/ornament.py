from turtle import Turtle, tracer, update, mainloop
from math import sqrt


#http://logia.oeiizk.waw.pl/nowa/pliki/L161zad.pdf
#17:25
#21.2.2017
#Maksymilian Sobiech(-:
szerokosc = 500
p = Turtle()
wyp_liscia = "green"
kontur = "black"
def lisc(a):
    #rysuje jeden lisc z ornamentu(rysunek pomocniczy)
    a2 = a*2
    dl = 2.5*a*sqrt(3)/3*2
    p.pu()
    p.fd(dl)
    p.rt(180 - 30)
    p.pd()
    p.begin_fill()
    p.color(kontur, wyp_liscia)
    for i in range(3):
        #rysuje jeden bok liscia
        p.fd(a2)
        p.lt(90)
        p.fd(a)
        p.lt(90)
        p.fd(a)
        p.rt(30)
        p.fd(a)
        p.rt(120)
        p.fd(a)
        p.lt(30)
        p.fd(a)
        for m in range(3):
            #rysuje kolce na gorze liscia
            p.lt(60)
            p.fd(a)
            p.rt(120)
            p.fd(a)
        p.lt(60)
        p.fd(a)
        p.lt(60)
        p.fd(a)
        p.rt(120)
        p.fd(a)
        p.rt(60)
        p.fd(a)
        p.lt(90)
        p.fd(a)
        p.lt(90)
        p.fd(a2)
        p.rt(120)
    p.end_fill()
    p.rt(30)
    p.pu()
    p.fd(dl)

def ornament(n):
    a = szerokosc/(n*5+(5*(n-1)))
    p.pu()
    p.bk(szerokosc/2-2.5*a)
    p.pu()
    il = 1
    for i in range(n):
        if il%2 == 0 :
            p.seth(270)
            lisc(a)
            p.seth(0)
            p.fd(a*10)
            p.pd()
        else:
            p.seth(90)
            lisc(a)
            p.seth(0)
            p.fd(a * 10)
            p.pd()
        il += 1


tracer(0)
ornament(3)
update()
mainloop()
#18:32