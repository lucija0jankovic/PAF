import matplotlib.pyplot as plt
import math

class Particle:
    def __init__(self,v0,kut,x0,y0):
        self.v0=v0
        self.kut=kut*math.pi/180
        self.x0=x0
        self.y0=y0

    def reset(self):
        self.x=[self.x0]
        self.y=[self.y0]
        self.vx=self.v0*math.cos(self.kut)
        self.vy=self.v0*math.sin(self.kut)
        self.t=[0.0]
        
    def __move(self,dt):
        self.g=9.81
        x=self.x[-1]+self.vx*dt
        vy=self.vy-self.g*dt
        y=self.y[-1]+self.vy*dt

        self.x.append(x)
        self.y.append(y)
        self.vy=vy
        self.t.append(self.t[-1]+dt)
    
    def range(self,dt=0.01):
        self.reset()

        while self.y[-1]>=0:
            self.__move(dt)

        domet=self.x[-1]-self.x0
        return domet
    
    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()