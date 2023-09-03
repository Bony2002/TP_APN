class Auto:
    def __init__(self,velocity,acceleration,adelante,atras,max_velocity,min_distance,position):
        self.thw=2
        self.dt=0.25

        self.maxacl=1
        self.atras=atras
        self.adelante=adelante
        self.pos=position

        self.vel=velocity
        self.acl=acceleration
        
        self.mindst=min_distance

        self.velmax=max_velocity

        self.nextvel=0
        self.nextacl=0
        self.nextpos=0

        self.distraction=False

        self.desiredst=0
        self.newgap=0
        self.gap=1000
        self.minacl=3
    def decision(self):
        gamma=4
        if self.adelante!=None:
            self.gap=self.adelante.pos - self.pos - 4
            self.desiredst= self.mindst + max(0, (self.vel*self.thw + (self.vel-self.adelante.vel)/2*(self.maxacl*self.minacl)**0.5))
        if self.distraction==False:
            self.nextacl= max(-5,self.maxacl*(1-(self.vel/self.velmax)**gamma - (self.desiredst/(self.gap))**2))
            self.nextpos= self.pos + self.vel*self.dt 
            self.nextvel= max(0, self.vel + (self.acl)*self.dt)

    def update(self):
        self.pos=self.nextpos
        self.acl=self.nextacl
        self.vel=self.nextvel
        

    def revision():
        #No se si se hace aca o lo hacemos en la lista en general.
        pass
