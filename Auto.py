class Auto:
    def __init__(self,velocity,acceleration,adelante,atras,max_velocity,min_distance,position):

        self.id = 0      

        self.pos=position # Cuado hagamos dos carriles debería ser una tupla
        self.vel=velocity
        self.acl=acceleration
        self.gap=1000

        self.atras=atras #Vehiculo que se ecuentra detras de self
        self.adelante=adelante #Vehiculo que se encuentra adelante de self
        
        self.thw=2 # Time Headway: El gap de tiempo entre que el frente de un vehículo pase por 
                   # un punto y el frente del vehículo que lo sigue pase por el mismo punto 
        self.dt=0.5 # Delta Time : Lapso de tiempo que se entá teniendo en cuenta durante la simulación

        self.maxacl=3.5# La máxima aceleración y desaceleracion posible para un auto
            
        self.mindst=min_distance # La mínima distancia medida en metros que deben tener dos vehículos entre si
        self.velmax=max_velocity # La velocidad máxima de la autopista/de la persona
        self.desiredst=0
        self.minacl=3
        self.distraction=False # Probabilidad de distracción

        # Valores de la velocidad, aceleración y posición que se calcula para alcanzar en el sigueinte momento
        self.nextvel=0
        self.nextacl=0
        self.nextpos=0
        self.newgap=0 ## Fijarse por qué esto no se utiliza
        
    def decision(self):
        gamma=4
        if self.adelante!=None:
            self.gap=self.adelante.pos - self.pos - 4
            self.desiredst= self.mindst + max(0, (self.vel*self.thw + (self.vel-self.adelante.vel)/2*(self.maxacl*self.minacl)**0.5))
        if self.distraction==False:
            self.nextacl= max(-self.maxacl,min(self.maxacl,1*(1-(self.vel/self.velmax)**gamma - (self.desiredst/(self.gap))**2)))
            self.nextpos= self.pos + self.vel*self.dt 
            self.nextvel= max(0, self.vel + (self.acl)*self.dt)

    def update(self):
        self.pos=self.nextpos
        self.acl=self.nextacl
        self.vel=self.nextvel
        

    def revision():
        #No se si se hace aca o lo hacemos en la lista en general.
        pass
