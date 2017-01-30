from time import clock
from turtle import Turtle, mainloop, tracer, update


def start(n):
    plist = []
    angle = 0
    p = Turtle()
    p.hideturtle()
    p.getscreen().tracer(30, 0)
    p.setundobuffer(None)
    plist.append(p)
    for i in range(n):
        q = p.clone()
        q.right(angle)
        plist.append(q)
        angle += (360 / n)
    star(plist)


def star(plist):
    for p in plist:
        p.fd(100)


def main():
    a = clock()
    tracer(30, 0)
    start(10)
    update()
    b = clock()

    return "done: %.2f sec." % (b - a)


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
