class Auto:
    def __init__(self,vel,acl,adelante,atras,velmax,mdist):
        self.thw=3
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
        self.gap=self.adelante.pos - self.pos -4
        self.distraction=False
    def decision(self):
        gamma=4
        self.desiredst= self.adelante.vel*self.thw 
        if self.distraction==False:
            self.nextacl= self.maxacl*(1-(self.vel/self.velmax)**gamma - (self.desiredst/(self.gap))**2)
        self.nextpos= self.pos + (self.vel)*self.dt
        self.nextvel= self.vel + (self.acl)*self.dt
        self.newgap= self.adelante.pos - self.pos -4


    def update(self):
        self.pos=self.nextpos
        self.acl=self.nextacl
        self.vel=self.nextvel
        self.gap=self.newgap

    def revision():
        #No se si se hace aca o lo hacemos en la lista en general.
        pass
