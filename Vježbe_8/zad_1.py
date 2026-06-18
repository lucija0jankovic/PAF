import numpy as np
import matplotlib.pyplot as plt

h0 = 0.54
m = 0.5257
r = 4.025e-3

h = [0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40]
t_mean = [1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813]

s = np.array(h)
t = np.array(t_mean)
g = 9.81
mr2 = m * (r**2)

def linearna_regresija(x, y):
    broj_tocaka = len(x)
    nazivnik = broj_tocaka * np.sum(x**2) - (np.sum(x))**2
    
    nagib = (broj_tocaka * np.sum(x * y) - np.sum(x) * np.sum(y)) / nazivnik
    odsjecak = (np.sum(y) * np.sum(x**2) - np.sum(x) * np.sum(x * y)) / nazivnik
    
    odstupanje = np.sum((y - (nagib * x + odsjecak))**2) / (broj_tocaka - 2)
    
    pogreska_nagiba = np.sqrt(odstupanje * broj_tocaka / nazivnik)
    pogreska_odsjecka = np.sqrt(odstupanje * np.sum(x**2) / nazivnik)
    
    return nagib, odsjecak, pogreska_nagiba, pogreska_odsjecka

# (a)
x_a = np.log(t)
y_a = np.log(s)
nagib_a, odsjecak_a, pogreska_nagiba_a, pogreska_odsjecka_a = linearna_regresija(x_a, y_a)

# (b)
x_b = t**2
y_b = s
nagib_b, odsjecak_b, pogreska_nagiba_b, pogreska_odsjecka_b = linearna_regresija(x_b, y_b)

# (c)
a_ef_a = 2 * np.exp(odsjecak_a)
pogreska_a_ef_a = a_ef_a * pogreska_odsjecka_a
Iz_a = mr2 * (g / a_ef_a - 1)
pogreska_Iz_a = mr2 * (g / (a_ef_a**2)) * pogreska_a_ef_a

a_ef_b = 2 * nagib_b
pogreska_a_ef_b = 2 * pogreska_nagiba_b
Iz_b = mr2 * (g / a_ef_b - 1)
pogreska_Iz_b = mr2 * (g / (a_ef_b**2)) * pogreska_a_ef_b

print("a")
print(f"Nagib:    {nagib_a:.4f} ± {pogreska_nagiba_a:.4f}")
print(f"Odsječak: {odsjecak_a:.4f} ± {pogreska_odsjecka_a:.4f}\n")

print("b")
print(f"Nagib:    {nagib_b:.4f} ± {pogreska_nagiba_b:.4f}")
print(f"Odsječak: {odsjecak_b:.4f} ± {pogreska_odsjecka_b:.4f}\n")

print("c")
print(f"Iz (log-log) = ({Iz_a*1e4:.2f} ± {pogreska_Iz_a*1e4:.2f}) * 10^-4 kg m^2")
print(f"Iz (s - t^2) = ({Iz_b*1e4:.2f} ± {pogreska_Iz_b*1e4:.2f}) * 10^-4 kg m^2")

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(x_a, y_a, 'ro')
plt.plot(x_a, nagib_a * x_a + odsjecak_a, 'b-')
plt.xlabel('log(t)')
plt.ylabel('log(s)')

plt.subplot(1, 2, 2)
plt.plot(x_b, y_b, 'ro')
plt.plot(x_b, nagib_b * x_b + odsjecak_b, 'b-')
plt.xlabel('t^2 (s^2)')
plt.ylabel('s (m)')

plt.tight_layout()
plt.show()

#koristen ai