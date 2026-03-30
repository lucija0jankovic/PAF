import matplotlib.pyplot as plt

def pravac():

    def unos(poruka):
        while True:
            try:
                broj=float(input(poruka))
                return broj
            except:
                print('unesi broj')

    x1 = unos('unesi x1: ')
    y1 = unos('unesi y1: ')
    x2 = unos('unesi x2: ')
    y2 = unos('unesi y2: ')

    if x1 == x2:
        print(f'jednadzba pravca je x={x1}')
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print('jednadžba pravca je y =', k, '* x +', l)

    

    x = [x1, x2]
    y = [y1, y2]

    plt.plot(x, y)

    izbor = input('za spremit napisi s, a za prikazat napisi p')

    if izbor == 'p':
        plt.show()
    else:
        ime = input('ime datoteke?')
        plt.savefig(ime + '.pdf')
        print('pdf spremljen')

pravac()
