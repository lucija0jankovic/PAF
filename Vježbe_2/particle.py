import matplotlib.pyplot as plt
import math

class Particle:
    def __init__(self,v0,kut,x0,y0):
        self.v0=v0
        self.kut=kut*math.pi/180
        self.x0=x0
        self.y0=y0

    def reset(self):
        self.x=self.x0
        self.y=self.y0

        self.vx=self.v0 * math.cos(self.kut)
        self.vy=self.v0 * math.sin(self.kut)
        self.t=0

        self.x_lista=[self.x]
        self.y_lista=[self.y]
        
    def __move(self,dt):
        g=9.81

        self.x+=self.vx * dt
        self.y+=self.vy * dt

        self.vy-=g * dt 
        self.t+=dt

        self.x_lista.append(self.x)
        self.y_lista.append(self.y)
    
    def range(self,dt=0.01):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x
    
    
    def plot_trajectory(self,dt=0.01):
        self.reset()
        while self.y >= 0:
            self.__move(dt)

        plt.plot(self.x_lista,self.y_lista)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()