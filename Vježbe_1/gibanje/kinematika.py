import matplotlib.pyplot as plt

def jednoliko_gibanje(F,m):
    t_max=10
    dt=0.01
    a=F/m
    
    t=0
    x=0
    v=0
    
    vrijeme = []
    x_lista = []
    v_lista = []
    a_lista = []
    
    while t<=t_max:
        vrijeme.append(t)
        x_lista.append(x)
        v_lista.append(v)
        a_lista.append(a)
        
        x=x+v*dt
        v=v+a*dt
        t=t+dt
    
    

    plt.subplot(3, 1, 1)
    plt.plot(vrijeme, x_lista)
    plt.xlabel('t(s)')
    plt.ylabel('x(m)')
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(vrijeme, v_lista)
    plt.xlabel('t(s)')
    plt.ylabel('v(m/s)')
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(vrijeme, a_lista)
    plt.xlabel('t(s)')
    plt.ylabel('a(m/s²)')
    plt.grid(True)

   
    plt.show()  