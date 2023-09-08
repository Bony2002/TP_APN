import numpy as np
import Autopista
class Auto:
    def __init__(self,id,position,velocity,acceleration,max_velocity,responsable):

        self.id = id # id del auto

        self.pos = position # Posición del auto en la autopista (metros)
        self.vel = velocity # Velocidad actual del auto (m/s)
        self.acl = acceleration # Aceleración actual del auto (m/s**2)
        self.gap = 1000 # Espacio entre el auto (self) y el auto que se encuentra adelante.
                      #
                      # Se setea en 1000 como una exageración de número grande para representar
                      # al primer auto quien no tiene autos adelante

        self.adelante = None # Vehiculo que se encuentra adelante de self
        self.atras = None # Vehiculo que se ecuentra detras de self

        self.max_acl = 3  # Máxima aceleración física posible para un auto
        self.max_dacl = 4   # La máxima desaceleración física posible para un auto

        self.dt = 0.5 # Delta Time : Lapso de tiempo que se está teniendo en cuenta durante la simulación


        self.choque=0
        self.cooldownchoque=0


        # Se me ocurre que se puede plantear lo siguiente: el objetivo de cada persona es una escala donde se van a balancear dos aspectos:
        # Llegar lo antes posible y de manera segura. Estos aspectos se van a medir en valores del [0:1] de manera que 
        # el conductor óptimo va a querer tener "Llegar lo antes posible" en 1 y de mnaer segura en 1 pero puede ser que por ejemplo haya una persona
        # que no le interese llegar de manera segura pero si lo antes posible, lo que haría que esta persoan vaya a una mayor velocidad de la permitida en la autopista
        # La responsabilidad del conductor, su velocidad máxima y su aceleración dependen de estos valores

        if responsable==True:
            self.druido=0.1
            self.exp=1
            self.thw=2 # Time Headway: El gap de tiempo entre que el frente de un vehículo pase por un punto y el frente del vehículo que lo sigue pase por el mismo punto 
            self.mindst=5 # La mínima distancia medida en metros que deben tener dos vehículos entre si
        else:
            self.thw=1.5
            self.druido=0.5
            self.exp=3
            self.mindst=2 # La mínima distancia medida en metros que deben tener dos vehículos entre si

        self.velmax=max_velocity # La velocidad máxima de la persona
        self.desiredst=0
        self.distraction=False # Probabilidad de distracción

        # Valores de la velocidad, aceleración y posición que se calcula para alcanzar en el siguiente momento
        self.nextvel=0
        self.nextacl=0
        self.nextpos=0
        self.newgap=0 ## Fijarse por qué esto no se utiliza
        
    def revision(self,Autopista):
        if self.adelante!=None:
            if self.cooldownchoque==10:
                Autopista.eliminar(self.id)
                self.choque=0
            elif self.pos - self.pos.adelante < 4  and self.choque==0:
                self.choque=1
                self.adelante.choque=1
                self.vel=0
                self.acl=0
                self.adelante.vel=0
                self.adelante.acl=0
            elif self.choque==1:
                self.cooldownchoque+=1


    def decision(self):
        error=np.random.normal(0,self.druido,1).item
        gamma=4
        if self.adelante != None:
            self.desiredst = self.mindst + max(0, (self.vel*self.thw + (self.vel-self.adelante.vel)/2*(self.max_acl*self.max_dacl)**0.5))
        if self.distraction == False:
            self.nextacl = max(-self.max_dacl,min(self.max_acl,self.max_acl*(1-(self.vel/self.velmax)**gamma - (self.desiredst/(self.gap))**2 + error )))
            self.nextpos = self.pos + self.vel*self.dt +1/2*self.acl*self.dt**2
            self.nextvel = max(0, self.vel + (self.acl)*self.dt)

    def update(self):
        self.pos = self.nextpos
        self.acl = self.nextacl
        self.vel = self.nextvel
        if self.adelante != None:
            self.gap = self.adelante.pos - self.pos - 4

        


        
        
