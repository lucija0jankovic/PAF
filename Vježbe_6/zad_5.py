import math
import numpy as np
def srednja_vrijednost(podaci):
    n=len(podaci)
    srednja=sum(podaci)/n
    return srednja

def devijacija_n(podaci):
    n=len(podaci)
    srednja=srednja_vrijednost(podaci)
    suma_kvadrata=sum((x-srednja)**2 for x in podaci)
    sig_n=math.sqrt(suma_kvadrata/n)
    return sig_n

def devijacija_n_minus_1(podaci):
    n=len(podaci)
    srednja=srednja_vrijednost(podaci)
    suma_kvadrata=sum((x-srednja)**2 for x in podaci)
    s=math.sqrt(suma_kvadrata/(n-1))
    return s

def pogreska_srednje(podaci):
    n=len(podaci)
    s=devijacija_n_minus_1(podaci)
    sig_x_bar=s/math.sqrt(n)
    return sig_x_bar

malo_n=[99.8,100.1,99.9,100.2,100.0]

np.random.seed(42)
veliko_n=np.random.normal(loc=100.0,scale=0.2,size=10000).tolist()

m_sig_n=devijacija_n(malo_n)
m_s=devijacija_n_minus_1(malo_n)
m_sig_x_bar=pogreska_srednje(malo_n)

v_sig_n=devijacija_n(veliko_n)
v_s=devijacija_n_minus_1(veliko_n)
v_sig_x_bar=pogreska_srednje(veliko_n)

print("malo n:")
print(f"prva devijacija:{m_sig_n}")
print(f"druga devijacija:{m_s}")
print(f"pogreska srednje:{m_sig_x_bar}")

print("veliko n:")
print(f"prva devijacija:{v_sig_n}")
print(f"druga devijacija:{v_s}")
print(f"pogreska srednje:{v_sig_x_bar}")

