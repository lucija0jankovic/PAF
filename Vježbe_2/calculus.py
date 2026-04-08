#3_zad

import numpy as np

def derivacija(f, x, epsilon=1e-5, metoda='three-step'):

    if metoda=='two-step':
        return (f(x + epsilon) - f(x))/epsilon
    else:
        return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

def derivacija_interval(f, a, b, n=100, epsilon=1e-5, metoda='three-step'):
    x_lista=np.linspace(a,b,n)
    derivacije=[]
    
    for x in x_lista:
        derivacije.append(derivacija(f,x,epsilon,metoda))
    
    return x_lista, derivacije

#4_zad

def pravokutno(f, a, b, n):
    h=(b - a) / n
    ljeva_suma=0
    desna_suma=0

    for i in range(n):
        x1= a + i * h
        x2 = a + (i + 1) * h

        ljeva_suma += f(x1)
        desna_suma += f(x2)

    ljeva= ljeva_suma * h
    desna = desna_suma * h

    return ljeva, desna

def trapezna(f, a, b, n):
    h = (b - a) / n

    suma= f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        suma+= 2 * f(x)

    return (h / 2) * suma