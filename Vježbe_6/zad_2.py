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

def volumen_valjka(R, L):
    return (R ** 2) * math.pi * L

def sigma_volumena(R, sigma_R, L, sigma_L):
    dV_dR = 2 * math.pi * R * L
    dV_dL = math.pi * (R ** 2)
    return math.sqrt((dV_dR * sigma_R) ** 2 + (dV_dL * sigma_L) ** 2)

dijametri = {
    1: [19.98, 20.18, 20.10, 20.08, 19.74],
    2: [19.92, 19.82, 19.96, 19.98, 19.88],
    3: [24.96, 24.98, 24.98, 24.92, 24.94]
}

duljine = {
    1: [49.80, 49.00, 50.48, 49.80, 49.96],
    2: [52.56, 52.50, 52.62, 52.58, 52.54],
    3: [55.34, 55.40, 55.30, 55.44, 55.48]
}

for i in [1, 2, 3]:
    radijusi=[]
    for d in dijametri[i]:
        r=d/2
        radijusi.append(r)
    
    R_srednja = srednja_vrijednost(radijusi)
    sigma_R = standardna_devijacija(radijusi)
    
    L_srednja = srednja_vrijednost(duljine[i])
    sigma_L = standardna_devijacija(duljine[i])
    
    R_cm = R_srednja / 10.0
    sigma_R_cm = sigma_R / 10.0
    L_cm = L_srednja / 10.0
    sigma_L_cm = sigma_L / 10.0
    
    V = volumen_valjka(R_cm, L_cm)
    s_V = sigma_volumena(R_cm, sigma_R_cm, L_cm, sigma_L_cm)
    
    print(f"valjak {i} V_srednja = {V:.2e} cm3")
    print(f"valjak {i} sigma_V   = {s_V:.2e} cm3")
