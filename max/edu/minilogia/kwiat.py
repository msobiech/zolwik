from turtle import Turtle, tracer, update, mainloop, circle, pos

p = Turtle()
promien = 150
def raczka(n):
    promien2 = promien/(n*2)
    for i in range(n):
        p.circle(promien2)
        p.lt(90)
        p.pu()
        p.fd(promien2*2)
        p.pd()
        p.rt(90)

def kwiat (n, x):
    bierzaca = pos()
    kat = 360/x
    for i in range(x):
        raczka(n)
        p.pu()
        p.goto(bierzaca)
        p.pd()
        p.rt(kat)

tracer(0)
kwiat(3 , 45)
update()
mainloop()