import math
import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, kut, g=9.81, c=0.1, m=1.0):
        self.v0 = v0
        self.kut=kut*math.pi/180
        self.g = g
        self.c = c
        self.m = m

    def _deriviranje(self, podaci):
        x, y, vx, vy = podaci
        v = np.sqrt(vx**2 + vy**2)

        ax = -(self.c / self.m) * v * vx
        ay = -self.g - (self.c / self.m) * v * vy
        
        return np.array([vx, vy, ax, ay])

    def euler(self, dt):
        podaci = np.array([0.0, 0.0, self.v0 * np.cos(self.kut), self.v0 * np.sin(self.kut)])
        rezultati = [podaci.copy()]
        
        while podaci[1] >= 0:
            deriv = self._deriviranje(podaci)
            podaci += deriv * dt
            rezultati.append(podaci.copy())
            
        return np.array(rezultati)

projectile = Projectile(v0=50.0, kut=45.0, c=0.1)
dt_list = [0.5, 0.1, 0.01]

plt.figure(figsize=(8, 5))

for dt in dt_list:
    putanja = projectile.euler(dt)
    plt.plot(putanja[:, 0], putanja[:, 1], label=f'Euler (dt = {dt} s)')

plt.title('Utjecaj vremenskog koraka na stabilnost Eulerove metode')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid(True)
plt.legend()
plt.show()
