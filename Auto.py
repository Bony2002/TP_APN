class Auto:
    def __init__(self,vel,acl,prev,prox,velmax,mdist):
        self.thw=3
        self.maxacl=1
        self.prox=prox
        self.prev=prev
        self.pos=0
        self.vel=vel
        self.acl=acl
        self.mindst=mdist
        self.velmax=velmax
        self.nextvel=0
        self.nextacl=0
        self.nextpos=0
        self.desiredst=0
    def decision(self,distraccion):
        gamma=4
        self.nextpos= self.pos + (self.vel)*0.5
        self.nextvel= self.vel + (self.acl)*0.5
        self.desiredst= self.prox.vel*self.thw 
        if distraccion:
            self.nextacl= self.maxacl*[1-(self.vel/self.velmax)**gamma - (self.desiredst/(self.pos-self.prev.pos))**2 ]
        pass

    def update(self):
        self.pos=self.nextpos
        self.acl=self.nextacl
        self.vel=self.nextvel
        pass

    def revision():
        #No se si se hace aca o lo hacemos en la lista en general.
        pass
