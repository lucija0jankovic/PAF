import numpy as np

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

a = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6] 
b = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6 , 5]

def medijan(podaci):
    x = sorted(podaci)
    n = len(x)

    if n % 2 != 0:
        rezultat = x[((n + 1) // 2) - 1]
    else:
        rezultat = (x[(n // 2) - 1] + x[(n // 2 + 1) - 1]) / 2
    return rezultat
    
print(f'medijan za parne = {medijan(a)}')
print(f'medijan za neparne = {medijan(b)}')

za_mase=medijan(mase)
provjera=np.median(mase)

print(f'rezultat sa funkc meidjan= {za_mase}')
print(f'pomocu numpy.median={provjera}')
