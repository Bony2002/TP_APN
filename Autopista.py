import Auto
import SDC
import numpy as np
class Autopista:
    def __init__(self,max_velocity,longitud,hora,carril): # La autopista esta definida como una lista enlazada, donde cada nodo es un auto
        self.primero = None
        self.ultimo = None
        self.hora = hora # Hora del día en la que se está simulando
        self.max_velocity_t1 = max_velocity # Velocidad máxima permitida en la autopista (m/s)
        self.max_velocity_t2 = max_velocity + 4.7778 # Velocidad máxima permitida en el segundo tramo de la autopista (m/s) 
        self.longitud = longitud # Longitud de la autopista (metros)
        self.carril = carril
        self.cant_autos=0
        self.carril = carril
        self.cant_multados = 0
        self.sdc_multados = 0
        self.recaudacion = 0

    def append(self, Auto): # Agrega un auto al final de la autopista
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
    
    
    def analisis(self): #Hace el analisis en todos los autos.
        if self.ultimo!=None:
            actual=self.ultimo
            while actual.adelante != None:
                actual.decision()
                actual=actual.adelante 
            actual.decision()

    def eliminar(self,id): #Elimina al auto segun el id
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

    def actualizacion(self): #Actualiza los estados de los autos
        positions = []
        carriles = []
        colores = []
        if self.ultimo!=None:
            actual=self.ultimo
            while actual.adelante != None:
                actual.update()
                positions.append(actual.pos)
                carriles.append(actual.carril.carril)
                colores.append(actual.color)
                actual=actual.adelante
            actual.update()
        return positions,carriles,colores

    def revision(self,t): #Realiza la revision en cada uno de los autos y se guarda distintos valores para realziar analisis.
        tiempo_terminacion = []
        tiempo_terminacion_SDC = []
        choques = []
        choques_SDC = []
        eliminar=False
        if self.ultimo!=None:
            actual=self.ultimo
            while actual.adelante != None:
                datos = actual.revision(self,t)
                if len(datos) != 0:
                    if actual.sdc == True:
                        choques_SDC.append(datos)
                    elif actual.sdc==False:
                        choques.append(datos)
                if actual.terminado==1 :
                    if actual.sdc == True:
                        tiempo_terminacion_SDC.append(t-actual.tiempo_entrada)    
                    elif actual.sdc == False:
                        tiempo_terminacion.append(t-actual.tiempo_entrada)
                    id_eliminar = actual.id
                    eliminar=True
                actual=actual.adelante
                if eliminar==True :
                    self.eliminar(id_eliminar)
            datos = actual.revision(self,t)
            if len(datos) != 0:
                    choques.append(datos)
            if actual.pos > 24300 and actual.terminado==0 :
                    self.terminado=1
                    tiempo_terminacion.append(t-actual.tiempo_entrada)
                    self.eliminar(actual.id)
        return (tiempo_terminacion,tiempo_terminacion_SDC),(choques,choques_SDC)

    def resumen(self): #Devuelve un resumen de la situacion actual.
        actual=self.ultimo
        resumen=np.zeros(shape=[self.cant_autos,4])
        i=0
        while actual.adelante!=None:
            resumen[i]=[actual.id,actual.pos,actual.vel,actual.acl]
            actual=actual.adelante
            i+=1
        resumen[i]=[actual.id,actual.pos,actual.vel,actual.acl]
        return resumen
    
    def query(self,posicion): # Segun tu posicion, busca en el carril cual es el auto de adelante y cual el de atras (se usa para el LC)
        actual = self.ultimo
        if actual == None:
            return False, False
        while(actual.pos<posicion):
            actual=actual.adelante
            if actual == None:
                break
        if  actual != None and actual.atras != None:
            return actual.atras,actual
        else:
            return False, False