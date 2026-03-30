class Particle:
    def __init__(self, v0, kut, x0, y0):
        self.v0=v0
        self.kut=kut
        self.x0=x0
        self.y0=y0

    def printInfo(self):
        print('pocetna brzina: ',self.v0)
        print('kut otklona:' , self.kut)
        print('pocetni x0: ',self.x0)
        print('pocetni y0: ',self.y0)
        

    def reset(self):
        self.__init__()

    def move(self, dt):
        self.x0+=dt 
        self.y0+=dt 

p1=Particle(10,50,5,6)
p1.move(0.01)
p1.printInfo()

