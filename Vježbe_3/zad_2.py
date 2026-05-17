import math
import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, kut, g=9.81, c=0.1, m=1.0):
        self.v0 = v0
        self.kut = kut * math.pi / 180
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

    def range_kut4(self, dt):
        podaci = np.array([0.0, 0.0, self.v0 * np.cos(self.kut), self.v0 * np.sin(self.kut)])
        rezultati = [podaci.copy()]
        
        while podaci[1] >= 0:
            k1 = self._deriviranje(podaci)
            k2 = self._deriviranje(podaci + 0.5 * dt * k1)
            k3 = self._deriviranje(podaci + 0.5 * dt * k2)
            k4 = self._deriviranje(podaci + dt * k3)
            
            podaci += (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            rezultati.append(podaci.copy())
            
        return np.array(rezultati)

projectile = Projectile(v0=50.0, kut=45.0, c=0.1)
dt_fiksni = 0.01


putanja_euler = projectile.euler(dt_fiksni)
putanja_rk4 = projectile.range_kut4(dt_fiksni)

plt.figure(figsize=(8, 5))
plt.plot(putanja_euler[:, 0], putanja_euler[:, 1], 'r--', linewidth=2, label=f'Eulerova metoda (dt = {dt_fiksni})')
plt.plot(putanja_rk4[:, 0], putanja_rk4[:, 1], 'b-', alpha=0.6, linewidth=2, label=f'RK4 metoda (dt = {dt_fiksni})')

plt.title('Zadatak 2: Usporedba putanja (Euler vs RK4) za dt = 0.01')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid(True)
plt.legend()
plt.show()
