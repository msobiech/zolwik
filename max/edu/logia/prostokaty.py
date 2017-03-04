from turtle import Turtle, tracer, update, mainloop

samogloski = ["a", "e", "y", "i", "o"]
spolgloski = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z']
wysoko = [ 'b', 'd', 'f', 'h', 'k', 'l', 't', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dol1 = ['g', 'j', 'p', 'q', 'y']
cyfry = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
bok = 25
p = Turtle()
def prostokat(kolor1):
    p.begin_fill()
    p.color("black", kolor1)
    for i in range(2):
        p.fd(bok)
        p.lt(90)
        p.fd(bok*2)
        p.lt(90)
    p.end_fill()


def do(kolor1):
    p.begin_fill()
    p.color("black", kolor1)
    p.rt(90)
    for i in range(2):
        for r in range(3):
            p.fd(bok)
            p.lt(90)
        p.rt(90)
    p.end_fill()
    p.lt(90)

def kwadrat(kolor1):
    p.begin_fill()
    p.color("black", kolor1)
    for i in range(4):
        p.fd(bok)
        p.lt(90)
    p.end_fill()


def rysuj(slowo):
    p.bk(len(slowo)/2*bok)
    for znak in slowo:
        kolor = "white"
        #wybor koloru
        if znak in samogloski:
            kolor = "red"
        elif znak in spolgloski:
            kolor = "yellow"
        elif znak in cyfry:
            kolor = "green"
         #wybor i rysowanie figury
        if znak in wysoko:
            prostokat(kolor)
        elif znak in dol1:
            do(kolor)
        elif kolor != "white":
            kwadrat(kolor)
        p.pu()
        p.fd(bok)
        p.pd()



tracer(0)
rysuj("2krokodyle")
update()
mainloop()