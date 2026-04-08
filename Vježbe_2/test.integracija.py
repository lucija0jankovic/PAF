import numpy as np
import matplotlib.pyplot as plt
import calculus

def f(x):
    return x**2

analiticki=8/3

a = 0
b = 2
analiticki=8/3
ljeve=[] 
desne=[]
trapezne=[]
n=[5, 10, 50]

for i in n:
    ljeva, desna = calculus.pravokutno(f, a, b, i)
    trap = calculus.trapezna(f, a, b, i)

    ljeve.append(ljeva)
    desne.append(desna)
    trapezne.append(trap)

    print("n =", i)
    print("Pravokutna donja:", ljeva)
    print("Pravokutna gornja:", desna)
    print("Trapezna:", trap)
    print()


plt.axhline(analiticki, label='analiticki') 
plt.plot(n, ljeve, label='ljeva')
plt.plot(n, desne, label='sesna')
plt.plot(n, trapezne, label='trapezna')

plt.legend() 
plt.show()