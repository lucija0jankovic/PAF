import numpy as np

def indeks_loma(valna_duljina, A, B):
    valna_duljina_um = valna_duljina / 1000.0
    return A + B / valna_duljina_um**2

def devijacija_za_jedan_kut(kut_upada, kut_prizme, valna_duljina, A_cauchy, B_cauchy):
    n = indeks_loma(valna_duljina, A_cauchy, B_cauchy)
    A = np.radians(kut_prizme)
    
    upadni_ulazni = np.radians(kut_upada)
    lomni_ulazni = np.arcsin(np.sin(upadni_ulazni) / n)
    upadni_izlazni = A - lomni_ulazni
    
    if abs(n * np.sin(upadni_izlazni)) <= 1.0:
        lomni_izlazni = np.arcsin(n * np.sin(upadni_izlazni))
        delta = np.degrees(upadni_ulazni + lomni_izlazni - A)
        return delta
    return None

def devijacija(kutovi_upada, kut_prizme, valna_duljina, A_cauchy, B_cauchy):
    n = indeks_loma(valna_duljina, A_cauchy, B_cauchy)
    A = np.radians(kut_prizme)
    validni_kutovi = []
    devijacije = []
    
    for i in kutovi_upada:
        upadni_ulazni = np.radians(i)
        lomni_ulazni = np.arcsin(np.sin(upadni_ulazni) / n)
        upadni_izlazni = A - lomni_ulazni
        
        if abs(n * np.sin(upadni_izlazni)) <= 1.0:
            lomni_izlazni = np.arcsin(n * np.sin(upadni_izlazni))
            delta = np.degrees(upadni_ulazni + lomni_izlazni - A)
            validni_kutovi.append(i)
            devijacije.append(delta)
            
    return validni_kutovi, devijacije

def putanja_zrake(kut_upada, kut_prizme, valna_duljina, A_cauchy, B_cauchy):
    n = indeks_loma(valna_duljina, A_cauchy, B_cauchy)
    upadni_ulazni = np.radians(kut_upada)
    A = np.radians(kut_prizme)  
    
    lomni_ulazni = np.arcsin(np.sin(upadni_ulazni) / n)
    upadni_izlazni = A - lomni_ulazni
    if abs(n * np.sin(upadni_izlazni)) > 1.0:
        return None
    lomni_izlazni = np.arcsin(n * np.sin(upadni_izlazni))
    
    L = 3.0
    y_ulaza = 0.8
    x_ulaza = y_ulaza / np.tan(A) 
    P_ulaza = np.array([x_ulaza, y_ulaza])
    kut_vani = A - upadni_ulazni 
    smjer_vani = np.array([np.cos(kut_vani), -np.sin(kut_vani)])
    P_pocetna = P_ulaza - smjer_vani 
    kut_unutra = A - lomni_ulazni 
    smjer_unutra = np.array([np.cos(kut_unutra), -np.sin(kut_unutra)])
    k_lom = smjer_unutra[1] / smjer_unutra[0]
    l_lom = P_ulaza[1] - k_lom * P_ulaza[0]
    kut_baze = np.radians((180.0 - kut_prizme) / 2.0)
    k2 = -np.tan(kut_baze)
    l2 = L * np.tan(kut_baze)
    Tx_2 = (l2 - l_lom) / (k_lom - k2)
    Ty_2 = k_lom * Tx_2 + l_lom
    P_izlaza = np.array([Tx_2, Ty_2])
    kut_izlaza = A + lomni_izlazni 
    
    kut_korekcije = np.radians(90.0) - kut_baze
    P_krajnja = P_izlaza + np.array([np.cos(kut_izlaza - kut_korekcije), -np.sin(kut_izlaza - kut_korekcije)]) * 2.5
    return np.array([P_pocetna, P_ulaza, P_izlaza, P_krajnja])
