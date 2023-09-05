from Auto import Auto
import numpy as np
class Autopista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cant_autos=0
    
    def append(self, Auto):
        nuevo_auto = Auto
        self.cant_autos+=1
        if not self.primero:
            self.primero = nuevo_auto
            self.ultimo = nuevo_auto
        else:
            nuevo_auto.gap=self.ultimo.pos - nuevo_auto.pos - 4
            nuevo_auto.adelante = self.ultimo
            self.ultimo.atras = nuevo_auto
            self.ultimo = nuevo_auto
    
    
    def analisis(self):
        if self.ultimo!=None:
            actual=self.ultimo
            while actual.adelante != None:
                actual.decision()
                actual=actual.adelante 
            actual.decision()

    def eliminar(self,id):
        fin=False
        actual=self.ultimo
        while actual!=None and fin==False:
            if actual.id == id:
                fin=True
                if actual.atras!=None:
                   actual.atras.adelante = actual.adelante
                if actual.adelante!=None:
                    actual.adelante.atras = actual.atras
            actual=actual.adelante

    def actualizacion(self):
        actual=self.ultimo
        while actual.adelante != None:
            actual.update()
            actual=actual.adelante    
        actual.update()
    def revision(self,t):
        pass

    def resumen(self):
        actual=self.ultimo
        resumen=np.zeros(shape=[self.cant_autos,4])
        i=0
        while actual.adelante!=None:
            resumen[i]=[actual.id,actual.pos,actual.vel,actual.acl]
            actual=actual.adelante
            i+=1
        resumen[i]=[actual.id,actual.pos,actual.vel,actual.acl]
        return resumen

