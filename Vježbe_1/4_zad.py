koordinate = []

for i in ['x1', 'y1', 'x2', 'y2']:
    unos = input(f'unesi {i} ')
    while not unos.replace('.', '', 1).isdigit():
        print('ponovo unesi')
        unos = input(f'unesi {i} ')
    koordinate.append(float(unos))

x1, y1, x2, y2 = koordinate

def pravac(x1, y1, x2, y2):
    if x1 == x2:
        print(f'jednadzba pravca je x={x1}')
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print(f'jednadžba pravca y = {k}x + {l}')

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
    if x1 == x2:
        print(f'jednadzba pravca je x={x1}')
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print(f'jednadžba pravca y = {k}x + {l}')

pravac(x1, y1, x2, y2)
