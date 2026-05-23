import math

def srednja_vrijednost(podaci):
    n=len(podaci)
    srednja=sum(podaci)/n
    return srednja

def standardna_devijacija(podaci):
    n = len(podaci)
    srednja = srednja_vrijednost(podaci)
    suma_kvadrata=sum((x-srednja)**2 for x in podaci)
    sigma=math.sqrt(suma_kvadrata/(n*(n-1)))
    return sigma

promjeri = {
    1: [19.98, 20.18, 20.10, 20.08, 19.74],
    2: [19.92, 19.82, 19.96, 19.98, 19.88],
    3: [24.96, 24.98, 24.98, 24.92, 24.94]
}

duljine = {
    1: [49.80, 49.00, 50.48, 49.80, 49.96],
    2: [52.56, 52.50, 52.62, 52.58, 52.54],
    3: [55.34, 55.40, 55.30, 55.44, 55.48]
}

mase = {
    1: [138.92, 138.98, 139.20, 138.90, 138.92],
    2: [128.65, 128.60, 128.65, 128.35, 128.50],
    3: [71.89, 71.90, 71.79, 71.85, 71.70]
}

for i in [1, 2, 3]:
    radijusi = [d / 2.0 for d in promjeri[i]]
    
    R_srednja = srednja_vrijednost(radijusi)
    sigma_R = standardna_devijacija(radijusi)
    
    L_srednja = srednja_vrijednost(duljine[i])
    sigma_L = standardna_devijacija(duljine[i])
    
    m_srednja = srednja_vrijednost(mase[i])
    sigma_m = standardna_devijacija(mase[i])
    
    print(f"\nvaljak {i}:")
    print(f"R_srednja = {R_srednja:.4f} mm, sigma_R = {sigma_R:.4f} mm")
    print(f"L_srednja = {L_srednja:.4f} mm, sigma_L = {sigma_L:.4f} mm")
    print(f"m_srednja = {m_srednja:.4f} g, sigma_m = {sigma_m:.4f} g")
