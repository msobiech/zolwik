
def trojki(zakres, suma):
    for a in range(1, zakres+1):
        for b in range(1, zakres+1):
            for c in range(1, zakres+1):
                su = a + b + c
                if su == suma and a < b < c:
                    print(str(a) + " " + str(b) + " " + str(c))

trojki(3, 6)