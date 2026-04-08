from particle import Particle
import math

p1=Particle(100, 50, 0, 0)
domet_numericki=p1.range()
g=9.81
domet_analiticki=(p1.v0**2*math.sin(2*p1.kut))/g
odstupanje = abs(domet_numericki - domet_analiticki)

print(f'numericki: {domet_numericki}')
print(f'analiticki: {domet_analiticki}')
print(f'odstupanje: {odstupanje}')

p1.plot_trajectory()