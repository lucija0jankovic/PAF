import numpy as np
import matplotlib.pyplot as plt
import calculus

# funkcija
def f(x):
    return x**2

# analitički integral
def analytical(a, b):
    return (b**3)/3 - (a**3)/3

a = 0
b = 2

n_values = [5, 10, 50]

# test integracije
for n in n_values:
    lower, upper = calculus.rectangle_integration(f, a, b, n)
    trap = calculus.trapezoidal_integration(f, a, b, n)

    print("n =", n)
    print("Pravokutna donja:", lower)
    print("Pravokutna gornja:", upper)
    print("Trapezna:", trap)
    print()

# analitičko rješenje
exact = analytical(a, b)
print("Analitički integral:", exact)

# graf funkcije
x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y)
plt.grid()
plt.show()