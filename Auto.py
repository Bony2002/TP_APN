class Auto:
    def __init__(self,vel,acl,velmax):
        self.pos=0
        self.vel=vel
        self.acl=acl
        self.velmax=velmax
        self.nextvel=0
        self.nextacl=0
        self.nextpos=0
    def decision(self):
        self.nextpos= self.pos + (self.vel)*1  
        self.nextvel= self.vel + (self.acl)*1
        self.nextacl #A definir esto es la decision que hay que tomar (Cuanto acelero o desacelero)
        pass

    def update(self):
        self.pos=self.nextpos
        self.acl=self.nextacl
        self.vel=self.nextvel
        pass

    def revision():
        #No se si se hace aca o lo hacemos en la lista en general.
        pass
