koordinate = []

for i in ['x1', 'y1', 'x2', 'y2']:
    unos = input(f'unesi {i} ')
    while not unos.replace('.', '', 1).isdigit():
        print('ponovo unesi')
        unos = input(f'unesi {i} ')
    koordinate.append(float(unos))

x1, y1, x2, y2 = koordinate

if x1 == x2:
    print(f'jednadzba pravca je x={x1}')
else:
    k = (y2 - y1)/(x2 - x1)
    b = y1 - k * x1
    print(f'jednadžba pravca y = {k}x + {b}')