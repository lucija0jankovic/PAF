import matplotlib.pyplot as plt
import math
from calculus import derivacija, derivacija_interval

def kubna(x):
    return x**3 - 2*x**2 + x

def kubna_deriv(x):
    return 3*x**2 - 4*x + 1

f = kubna
f_deriv = kubna_deriv
pocetak, kraj = -2, 3

epsilon = [1e-1, 1e-3, 1e-5]
metode = ['three-step', 'two-step']

x_analiticki = [x/100 for x in range(int(pocetak*100), int(kraj*100)+1)]
y_analiticki = [f_deriv(x) for x in x_analiticki]

plt.plot(x_analiticki, y_analiticki, color='black')

for m in metode:
    for e in epsilon:
        xs, ys = derivacija_interval(f, pocetak, kraj, n=50, epsilon=e, metoda=m)
        plt.plot(xs, ys, '--o', markersize=2)

plt.xlabel('x')
plt.ylabel("f'(x)")
plt.show()