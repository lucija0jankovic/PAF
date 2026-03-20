x1 = float(input('unesi x1: '))
y1 = float(input('unesi y1: '))
x2 = float(input('unesi x2: '))
y2 = float(input('unesi y2: '))

def pravac(x1, y1, x2, y2):
    if x1 == x2:
        print('x1 i x2 ne smiju bit isti')
        return
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    print("y =", k, "* x +", l)

pravac(x1, y1, x2, y2)



#rjesen kao nastavak na treci

def unos(poruka):
    while True:
        try:
            broj = float(input(poruka))
            return broj
        except:
            print('unesi broj')


x1 = unos('unesi x1: ')
y1 = unos('unesi y1: ')
x2 = unos('unesi x2: ')
y2 = unos('unesi y2: ')

while x1 == x2:
    print('x1 i x2 ne smiju bit isti')
    x1 = unos('unesi x1: ')
    x2 = unos('unesi x2: ')


def pravac(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    print('jednadžba pravca je y =', k, '* x +', l)

pravac(x1, y1, x2, y2)
