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

k = (y2 - y1) / (x2 - x1)
l = y1 - k * x1

print('jednadžba pravca je y =', k, '* x +', l)

