import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
kut_rad = np.radians(kut_deg)

T_120 = np.array([0.8020 , 0.8187 , 0.8327 , 0.8660 , 0.8980 , 0.9153 , 0.9293 , 0.9653 ,
                  0.9747 , 1.0200 , 1.0373 , 1.1160 , 1.1780 , 1.2733 , 1.4180 , 1.6373 , 1.9100 , 2.5460])

T_240 = np.array([1.0140 , 1.0320 , 1.0433 , 1.0673 , 1.0840 , 1.1320 , 1.1440 , 1.1720 ,
                  1.1980 , 1.2293 , 1.2813 , 1.3573 , 1.4200 , 1.5600 , 1.7413 , 1.9840 , 2.4473 , 3.1573])

g = 9.81
L_mm_120 = 0.120
L_mm_240 = 0.240

def model_perioda(kut, l):
    return 2 * np.pi * np.sqrt(l / (g * np.cos(kut)))

parametri_120, _ = curve_fit(model_perioda, kut_rad, T_120, p0=[0.120])
l_120 = parametri_120[0]

parametri_240, _ = curve_fit(model_perioda, kut_rad, T_240, p0=[0.240])
l_240 = parametri_240[0]

rel_pogreska_120 = abs(l_120 - L_mm_120) / L_mm_120 * 100
rel_pogreska_240 = abs(l_240 - L_mm_240) / L_mm_240 * 100

print(f"Za L = 120 mm: izračunato l = {l_120*1000:.2f} mm, relativna pogreška = {rel_pogreska_120:.2f} %")
print(f"Za L = 240 mm: izračunato l = {l_240*1000:.2f} mm, relativna pogreška = {rel_pogreska_240:.2f} %")

kut_gusti_rad = np.linspace(0, np.radians(85), 100)
kut_gusti_deg = np.degrees(kut_gusti_rad)

plt.figure(figsize=(8, 6))
plt.plot(kut_deg, T_120, 'ro', label='mjerenja (120 mm)')
plt.plot(kut_gusti_deg, model_perioda(kut_gusti_rad, l_120), 'r-', label='teorija (120 mm)')

plt.plot(kut_deg, T_240, 'bo', label='mjerenja (240 mm)')
plt.plot(kut_gusti_deg, model_perioda(kut_gusti_rad, l_240), 'b-', label='teorija (240 mm)')

plt.xlabel('kut')
plt.ylabel('period')
plt.legend()
plt.show()

#koristen ai