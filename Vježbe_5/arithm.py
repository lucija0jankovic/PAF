import math
import numpy as np

tocke = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(tocke)

#a)

suma_x = 0.0
for x in tocke:
    suma_x += x
aritmeticka_sredina_a = suma_x / n

suma_kvadrata_razlika = 0.0
for x in tocke:
    suma_kvadrata_razlika += (x - aritmeticka_sredina_a) ** 2

nazivnik = n * (n - 1)
standardna_devijacija_a = (suma_kvadrata_razlika / nazivnik) ** 0.5

print(f"aritmetička sredina (a): {aritmeticka_sredina_a:.4f}")
print(f"standardna devijacija (a): {standardna_devijacija_a:.4f}\n")


#b)

aritmeticka_sredina_b = np.mean(tocke)

standardna_devijacija_b = np.std(tocke, ddof=1) / np.sqrt(n)

print(f"aritmetička sredina (b): {aritmeticka_sredina_b:.4f}")
print(f"standardna devijacija (b): {standardna_devijacija_b:.4f}")
