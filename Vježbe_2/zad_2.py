import math
import matplotlib.pyplot as plt
from particle import Particle
import numpy as np

v0=10
kut=60
g=9.81
theta=kut*math.pi/180
domet_analiticki=(v0**2*math.sin(2*theta))/g

p2=Particle(10,60,0,0)

domet_numericki=[]
greske=[]
dt_lista = []
dt_lista=np.linspace(0.001,0.1,100) 


for i in dt_lista:
    p2=Particle(10,60,0,0)
    numericki=p2.range(i)
    domet_numericki.append(numericki)

    greske.append(abs(numericki-domet_analiticki)/domet_analiticki*100)

plt.plot(dt_lista, greske, marker='o')


plt.grid()
plt.show()