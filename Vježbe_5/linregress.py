import matplotlib.pyplot as plt
import numpy as np

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
fi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])

n = len(M)

xy_sredina = np.mean(fi * M)
x2_sredina = np.mean(fi**2)
y2_sredina = np.mean(M**2)

a = xy_sredina / x2_sredina

sigma_a = np.sqrt((1 / n) * (y2_sredina / x2_sredina - a**2))

b = 0
y = a * fi + b

print("modul torzije Dt je =", a)
print("standardna pogreška σa je =", sigma_a)

plt.scatter(fi, M, color="red", label="Mjerenja")
plt.plot(fi, y, color="blue", label="Regresijski pravac")
plt.xlabel("fi")
plt.ylabel("M")
plt.legend()
plt.show()
