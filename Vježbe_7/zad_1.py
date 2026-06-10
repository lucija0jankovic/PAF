import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] 

def histogram(podaci, k):

    xmin = min(podaci)
    xmax = max(podaci)

    h = (xmax - xmin) / k

    rubovi = []
    for i in range(k + 1):
        rubovi.append(xmin + i * h)

    frekvencije = [0] * k

    for x in podaci:

        if x == xmax:
            frekvencije[k - 1] += 1
        else:
            indeks = int((x - xmin) / h)
            frekvencije[indeks] += 1

    print("Histogram:")

    for i in range(k):
        print(f"[{rubovi[i]:.3f}, {rubovi[i+1]:.3f}) : {frekvencije[i]}")

    return rubovi, frekvencije


rubovi, frekvencije = histogram(mase_ciste, 10)

sirina = rubovi[1] - rubovi[0]

plt.bar(rubovi[:-1], frekvencije, width=sirina, edgecolor="black")

plt.xlabel("masa")
plt.ylabel("broj zvijezda")
plt.title("histogram masa")

plt.show()