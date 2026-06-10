import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()

frekvencije_ugradeno, rubovi_ugradeno = np.histogram(mase_ciste, bins=10)


for i in range(len(frekvencije_ugradeno)):
    print(f"Razred {i+1} [{rubovi_ugradeno[i]:.2f}, {rubovi_ugradeno[i+1]:.2f}): {frekvencije_ugradeno[i]}")
print("vrjednosti su isto kao i u prvom zad")

aritmeticka_sredina = np.mean(mase_ciste)
medijan_vrijednost = np.median(mase_ciste)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)  
plt.hist(mase_ciste, bins=10, edgecolor='black', alpha=0.7, color='skyblue', label='Histogram (k=10)')
plt.axvline(aritmeticka_sredina, color='red', linestyle='dashed', linewidth=2, label=f'Sredina ({aritmeticka_sredina:.3f})')
plt.axvline(medijan_vrijednost, color='blue', linestyle='dotted', linewidth=2, label=f'Medijan ({medijan_vrijednost:.3f})')
plt.xlabel("masa")
plt.ylabel("frekvencija")
plt.title("k = 10")
plt.legend()

plt.subplot(1, 2, 2)  
plt.hist(mase_ciste, bins=5, edgecolor='black', alpha=0.7, color='salmon', label='Histogram (k=5)')
plt.axvline(aritmeticka_sredina, color='red', linestyle='dashed', linewidth=2, label=f'Sredina ({aritmeticka_sredina:.3f})')
plt.axvline(medijan_vrijednost, color='blue', linestyle='dotted', linewidth=2, label=f'Medijan ({medijan_vrijednost:.3f})')
plt.xlabel("msa")
plt.ylabel("fekvencija")
plt.title("k = 5")
plt.legend()

plt.tight_layout()
plt.show()
