import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
pogreske = [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]
mase = mase_ciste + pogreske

def medijan(podaci):
    x = sorted(podaci)
    n = len(x)
    if n % 2 != 0:
        rezultat = x[((n + 1) // 2) - 1]
    else:
        rezultat = (x[(n // 2) - 1] + x[(n // 2 + 1) - 1]) / 2
    return rezultat

aritmeticka_sredina = sum(mase) / len(mase)
za_mase = medijan(mase)

razlika = za_mase - aritmeticka_sredina
print(f"Razlika (sve): {razlika}")

mase_bez_pogreski = [x for x in mase if 1.5 <= x <= 2.5]

aritmeticka_sredina_cisto = sum(mase_bez_pogreski) / len(mase_bez_pogreski)
za_mase_cisto = medijan(mase_bez_pogreski)

print(
    f"sednja vrijednost se promijenila za: {abs(aritmeticka_sredina - aritmeticka_sredina_cisto)}"
)
print(f"mdijan se promijenio za: {abs(za_mase - za_mase_cisto)}")


plt.hist(mase, bins=30, range=(2, 2.5), edgecolor="black")
plt.axvline(x=aritmeticka_sredina,color="red",linestyle="--",label="aritm. sred s pogreskama",linewidth=1.5)
plt.axvline(x=za_mase, color="green", linestyle="--", label="mdijan sa pogreskama",linewidth=1.5, alpha=0.8)
plt.axvline(x=aritmeticka_sredina_cisto,color="darkred",linestyle="-",label="aritm. sred bez pogresaka", linewidth=1.5,alpha=0.6)
plt.axvline(x=za_mase_cisto,color="darkgreen",linestyle="-",label="mdijan bez pogresaka",linewidth=2)

plt.xlabel("masa uzoraka")
plt.ylabel("frekvencija")
plt.legend()
plt.show()
