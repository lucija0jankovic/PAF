#3_zad

import numpy as np

def derivacija(f, x, epsilon=1e-5, metoda='three-step'):

    if metoda=='two-step':
        return (f(x+epsilon)-f(x-epsilon))/(2*epsilon)
    else:
        return (-f(x+2*epsilon)+8*f(x+epsilon)-8*f(x-epsilon)+f(x-2*epsilon))/(12*epsilon)

def derivacija_raspon(f, a, b, n=100, epsilon=1e-5, metoda='three-step'):
    x_lista=np.linspace(a,b,n)
    derivacije=[]
    
    for x in x_lista:
        derivacije.append(derivacija(f,x,epsilon,metoda))
    
    return x_lista, derivacije

#4_zad
import numpy as np

# -----------------------------
# DERIVACIJA
# -----------------------------
def derivative(func, x, eps=0.01, method="three"):
    if method == "two":
        return (func(x + eps) - func(x - eps)) / (2 * eps)

    elif method == "three":
        return (-func(x + 2*eps) + 8*func(x + eps) - 8*func(x - eps) + func(x - 2*eps)) / (12 * eps)

    else:
        raise ValueError("Nepoznata metoda")


def derivative_range(func, x_min, x_max, step=0.1, eps=0.01, method="three"):
    x_values = np.arange(x_min, x_max, step)
    derivatives = []

    for x in x_values:
        derivatives.append(derivative(func, x, eps, method))

    return x_values, derivatives


# -----------------------------
# INTEGRACIJA - PRAVOKUTNA
# -----------------------------
def rectangle_integration(func, a, b, n):
    h = (b - a) / n

    lower_sum = 0
    upper_sum = 0

    for i in range(n):
        x_left = a + i * h
        x_right = a + (i + 1) * h

        lower_sum += func(x_left)
        upper_sum += func(x_right)

    lower = lower_sum * h
    upper = upper_sum * h

    return lower, upper


# -----------------------------
# INTEGRACIJA - TRAPEZNA
# -----------------------------
def trapezoidal_integration(func, a, b, n):
    h = (b - a) / n

    total = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        total += 2 * func(x)

    return (h / 2) * total