import numpy as np
import matplotlib.pyplot as plt
import prizma_modul as pm

raspon_upadnih = np.linspace(1, 90, 600)
valne_duljine = np.linspace(400, 700, 300)
norma = plt.Normalize(400, 700)
mapa_boja = plt.get_cmap('rainbow')

plt.figure(figsize=(15, 5))


plt.subplot(1, 3, 1)  
osi_upadni, osi_devijacija = pm.devijacija(raspon_upadnih, 60.0, 550.0, 1.5046, 0.0042)

devijacija_minimuma = min(osi_devijacija)
pozicija_minimuma = osi_devijacija.index(devijacija_minimuma)
kut_minimuma = osi_upadni[pozicija_minimuma]

plt.plot(osi_upadni, osi_devijacija)
plt.scatter(kut_minimuma, devijacija_minimuma, color='red')
plt.xlabel("Upadni kut")
plt.ylabel("Devijacija")


plt.subplot(1, 3, 2)  
devijacije_valnih = []
for valna_duljina in valne_duljine:
    skretanje = pm.devijacija_za_jedan_kut(45.0, 60.0, valna_duljina, 1.5046, 0.0042)
    devijacije_valnih.append(skretanje)

for i in range(len(valne_duljine) - 1):
    plt.plot(valne_duljine[i:i+2], devijacije_valnih[i:i+2], color=mapa_boja(norma(valne_duljine[i])))
plt.xlabel("Valna duljina")
plt.ylabel("Devijacija")

#usporedba materijala
plt.subplot(1, 3, 3)  
materijali = {"Voda": (1.324, 0.0032), "Akril": (1.480, 0.0050), "Krunsko staklo": (1.5046, 0.0042), "Flint staklo": (1.701, 0.0179), "Dijamant": (2.398, 0.0135)}

for kljuc, vrijednosti in materijali.items():
    A_mat, B_mat = vrijednosti
    osi_m_upadni, osi_m_devijacija = pm.devijacija(raspon_upadnih, 60.0, 550.0, A_mat, B_mat)
    plt.plot(osi_m_upadni, osi_m_devijacija, label=kljuc)

plt.xlabel("Upadni kut")
plt.ylabel("Devijacija")
plt.legend(loc='upper right')

plt.tight_layout()
plt.subplots_adjust(wspace=0.4)

plt.figure(figsize=(7, 6))

L = 3.0
H = L * np.sqrt(3) / 2
prizma_x = [0.0, L, L/2, 0.0]
prizma_y = [0.0, 0.0, H, 0.0]
plt.fill(prizma_x, prizma_y, color='#f2f8fc')
plt.plot(prizma_x, prizma_y, color='black', linewidth=1.5)

upadni_kut = 52.0
kut_prizme = 60.0
baza_stakla = 1.5046      
jacina_disperzije = 0.05

for valna_duljina in valne_duljine:
    put = pm.putanja_zrake(upadni_kut, kut_prizme, valna_duljina, baza_stakla, jacina_disperzije)
    if put is not None:
        plt.plot(put[:, 0], put[:, 1], color=mapa_boja(norma(valna_duljina)), linewidth=1.5, alpha=0.6)

plt.xlim(-1.5, 4.5)
plt.ylim(-1.0, 3.0)
plt.gca().set_aspect('equal')

plt.xlabel("X os")
plt.ylabel("Y os")
plt.title("simulacija prolaska zrake kroz prizmu")

plt.tight_layout()
plt.show()
