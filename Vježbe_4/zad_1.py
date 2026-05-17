import matplotlib.pyplot as plt
import numpy as np

m_e = 1.0
q_e = -1.0
q_p = 1.0

dt = 0.01
broj_koraka = 2000


def simuliraj(q, m, E, B):
    r = np.array([0.0, 0.0, 0.0])
    v = np.array([1.0, 1.0, 0.5])

    x, y, z = [], [], []

    for i in range(broj_koraka):
        x.append(r[0])
        y.append(r[1])
        z.append(r[2])

        a = (q / m) * (E + np.cross(v, B))

        v = v + a * dt
        r = r + v * dt

    return x, y, z


fig = plt.figure(figsize=(18, 6))


B1 = np.array([0.0, 0.0, 1.0])
E1 = np.array([0.0, 0.0, 0.0])
xe1, ye1, ze1 = simuliraj(q_e, m_e, E1, B1)
xp1, yp1, zp1 = simuliraj(q_p, m_e, E1, B1)

ax1 = fig.add_subplot(1, 3, 1, projection="3d")
ax1.plot(xe1, ye1, ze1, label="Elektron", color="blue")
ax1.plot(xp1, yp1, zp1, label="Pozitron", color="red")
ax1.set_title("1")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
ax1.legend()

B2 = np.array([0.0, 0.0, 1.0])
E2 = np.array([0.0, 0.0, 0.1])
xe2, ye2, ze2 = simuliraj(q_e, m_e, E2, B2)
xp2, yp2, zp2 = simuliraj(q_p, m_e, E2, B2)

ax2 = fig.add_subplot(1, 3, 2, projection="3d")
ax2.plot(xe2, ye2, ze2, label="Elektron", color="blue")
ax2.plot(xp2, yp2, zp2, label="Pozitron", color="red")
ax2.set_title("2 (E i B u Z-smjeru)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
ax2.legend()

B3 = np.array([0.0, 0.0, 1.0])
E3 = np.array([0.2, 0.0, 0.0])
xe3, ye3, ze3 = simuliraj(q_e, m_e, E3, B3)
xp3, yp3, zp3 = simuliraj(q_p, m_e, E3, B3)

ax3 = fig.add_subplot(1, 3, 3, projection="3d")
ax3.plot(xe3, ye3, ze3, label="Elektron", color="blue")
ax3.plot(xp3, yp3, zp3, label="Pozitron", color="red")
ax3.set_title("3 (E_x i B_z)")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_zlabel("Z")
ax3.legend()

plt.show()
