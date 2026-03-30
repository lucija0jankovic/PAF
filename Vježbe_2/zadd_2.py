import math
import matplotlib.pyplot as plt
from particle import Particle

v0=10
kut=60
g=9.81
theta=kut*math.pi/180
domet_analiticki=(v0**2*math.sin(2*theta))/g

dt_lista=[]
pogreska_lista=[]

p1 = Particle(v0,kut,0,0)

dt=0.1
while dt>=0.001:
    p1=Particle(v0,kut,0,0)
    domet_numericki=p1.range(dt)
    relativna_pogreska=abs(domet_numericki-domet_analiticki)/domet_analiticki*100
    print(f"dt: {dt:.4f} | Numericki: {domet_numericki:.4f} | Pogreska: {relativna_pogreska:.6f}%")

    dt_lista.append(dt)
    pogreska_lista.append(relativna_pogreska)
    
    dt = dt / 2

plt.figure(figsize=(10,6))
plt.plot(dt_lista,pogreska_lista,'bo-',linewidth=2,markersize=8)
plt.xlabel('vremenski korak dt (s)')
plt.ylabel('relativna pogreska (%)')
plt.xscale('log')
plt.yscale('log')
plt.show()