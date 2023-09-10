from Auto import Auto
import numpy as np
class Autopista:
    def __init__(self,max_velocity,longitud,hora,carril):
        self.primero = None
        self.ultimo = None
        self.hora = hora # Hora del día en la que se está simulando
        self.max_velocity = max_velocity # Velocidad máxima permitida en la autopista (m/s)
                                         # Hay que tener en cuenta el tramo que la maxima es 100km/h
        self.longitud = longitud # Longitud de la autopista (metros)
        self.carril = carril
        self.cant_autos=0
        self.p_entrar=0.6
    
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
        positions = []
        carriles = []
        if self.ultimo!=None:
            actual=self.ultimo
            while actual.adelante != None:
                actual.update()
                positions.append(actual.pos)
                carriles.append(actual.carril.carril)
                actual=actual.adelante
            actual.update()
        return positions,carriles

    def revision(self):
        if self.ultimo!=None:
            actual=self.ultimo
            while actual.adelante != None:
                actual.revision(self)
                actual=actual.adelante    
            actual.revision(self)

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
    
