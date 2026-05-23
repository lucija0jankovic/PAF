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
    V= (R ** 2) * math.pi * L
    return V

def sigma_volumena(R, sigma_R, L, sigma_L):
    dV_dR = 2 * math.pi * R * L
    dV_dL = math.pi * (R ** 2)
    s_V = math.sqrt((dV_dR * sigma_R) ** 2 + (dV_dL * sigma_L) ** 2)
    return s_V

def gustoca_valjka(m, V):
    ro=m/V
    return ro

def sigma_gustoce(m, sigma_m, V, sigma_V):
    dro_dm = 1 / V
    dro_dV = -m / (V ** 2)
    s_ro =math.sqrt((dro_dm * sigma_m) ** 2 + (dro_dV * sigma_V) ** 2)
    return s_ro

def relativna_pogreska(ro, ro_tablicna):
    razlika = abs(ro - ro_tablicna)
    pogreska = (razlika / ro_tablicna) * 100
    return pogreska

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

mase = {
    1: [138.92, 138.98, 139.20, 138.90, 138.92],
    2: [128.65, 128.60, 128.65, 128.35, 128.50],
    3: [71.89, 71.90, 71.79, 71.85, 71.70]
}


gustoce = {
    1: 8.96,  
    2: 7.85,  
    3: 2.70  }

materijali = {
    1: "bakar",
    2: "zeljezo / celik",
    3: "aluminij"

}

for i in [1, 2, 3]:
    radijusi = []
    for d in dijametri[i]:
        r = d / 2
        radijusi.append(r)
    
    R_srednja = srednja_vrijednost(radijusi)
    sigma_R = standardna_devijacija(radijusi)
    L_srednja = srednja_vrijednost(duljine[i])
    sigma_L = standardna_devijacija(duljine[i])
    
    m_srednja = srednja_vrijednost(mase[i])
    sigma_m = standardna_devijacija(mase[i])
    
    R_cm = R_srednja / 10.0
    sigma_R_cm = sigma_R / 10.0
    L_cm = L_srednja / 10.0
    sigma_L_cm = sigma_L / 10.0
    
    V = volumen_valjka(R_cm, L_cm)
    s_V = sigma_volumena(R_cm, sigma_R_cm, L_cm, sigma_L_cm)
    
    ro = gustoca_valjka(m_srednja, V)
    
    ro_tab = gustoce[i]
    pogreska = relativna_pogreska(ro, ro_tab)
    
    print(f"valjak {i} materijal      = {materijali[i]}")
    print(f"valjak {i} rel_pogreska   = {pogreska:.2f} %")
