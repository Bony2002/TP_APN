class Auto:
    def __init__(self,vel,acl,adelante,atras,velmax,mdist):
        self.thw=2
        self.dt=0.5
        self.maxacl=1
        self.atras=atras
        self.adelante=adelante
        self.pos=0
        self.vel=vel
        self.acl=acl
        self.mindst=mdist
        self.velmax=velmax
        self.nextvel=0
        self.nextacl=0
        self.nextpos=0
        self.desiredst=0
        self.distraction=False
        self.desiredst=3
        self.newgap=0
        self.gap=10000
    def decision(self):
        gamma=4
        if self.adelante!=None:
            self.desiredst= self.adelante.vel*self.thw 
        if self.distraction==False:
            self.nextacl= self.maxacl*(1-(self.vel/self.velmax)**gamma - (self.desiredst/(self.gap))**2)
            self.nextpos= self.pos + self.vel*self.dt 
            self.nextvel= max(0, self.vel + (self.acl)*self.dt)


    def update(self):
        self.pos=self.nextpos
        self.acl=self.nextacl
        self.vel=self.nextvel
        if self.adelante!=None:
            self.gap=self.adelante.pos - self.pos - 4

    def revision():
        #No se si se hace aca o lo hacemos en la lista en general.
        pass
