import numpy as np
import Autopista
class SDC:
    def __init__(self,id,tiempo_entrada,position,velocity,acceleration,carril,otro_carril):
        self.id = id # Id del auto
        self.sdc = True # Identificador de self driving car
        self.tiempo_entrada = tiempo_entrada
        self.carril = carril
        self.otro_carril = otro_carril
        self.adelante = None # Vehiculo que se encuentra adelante de self
        self.atras = None # Vehiculo que se ecuentra detras de self
        self.max_acl = 3  # Máxima aceleración física posible para un auto
        self.max_dacl = 4   # La máxima desaceleración física posible para un auto
        self.color="y"
        self.multa = 0

        self.dt = 0.5 # Delta Time : Lapso de tiempo que se está teniendo en cuenta durante la simulación
        self.pos = position # Posición del auto en la autopista (metros)
        self.vel = velocity # Velocidad actual del auto (m/s)
        self.acl = acceleration # Aceleración actual del auto (m/s**2)
        self.gap = 1000 # Espacio entre el auto (self) y el auto que se encuentra adelante.
                        # Se setea en 1000 como una exageración de número grande para representar
                        # al primer auto quien no tiene autos adelante
        self.choque = 0   # Esta chocado si/no
        self.cooldownchoque = 1 # Timer para retirar el choque
        self.cooldownLC = 0

        self.desiredvel = self.carril.max_velocity_t1 # La velocidad máxima a la que desea ir una persona

        self.time_hdw = 5.5 # Multiplicador del time headway que permite calcular el time_hdw dependiendo de la velocidad del auto
        self.mindst = 7 # La mínima distancia medida en metros que deben tener dos vehículos entre si
        self.personalidad = "SDC"

        # Valores de la velocidad, aceleración y posición que se calcula para alcanzar en el siguiente momento
        self.nextvel=0
        self.nextacl=0
        self.nextpos=0
        self.desiredst=0

        self.terminado = 0 # Bool que reprensemta cuando un auto llegó a destino
        self.tramo = 0 # Indicador del tramo de la Gral Paz en donde estoy: tramo = 0 maxima de 80 km/h - tramo = 1 maxima de 100 km/h

    def revision(self,Autopista,t):
        datos_choque=[]
        if self.pos > 24300:
            self.terminado=1
        if self.adelante!=None:
            if self.cooldownchoque == 0:
                Autopista.eliminar(self.id)
                self.choque = 0
            elif self.adelante.pos - self.pos < 4  and self.choque == 0:

                # print("hay dos que chocaron")
                # print("El auto ", self.id,"chocó a la velocidad",self.vel,"con el auto ",self.adelante.id,"a la velocidad de ",self.adelante.vel)
                # print("La posición en la que chocaron fue en :",self.pos,"\n")

                datos_choque = [self.id,self.vel,self.personalidad,self.adelante.id,self.adelante.vel,self.adelante.pos,self.adelante.personalidad,t]
                velocidad_impacto = max(self.vel,self.adelante.vel)
                self.cooldownchoque = 10 * velocidad_impacto**2
                self.choque = 1
                self.adelante.choque = 1
                self.vel = 0
                self.acl = 0
                self.adelante.vel = 0
                self.adelante.acl = 0
            elif self.choque == 1:
                self.cooldownchoque -= 1
        return datos_choque


    def decision(self):
        # Se recalcula la desired velocity porque en Gral. Paz hay un segundo tramos en donde la velocidad máxima es de 100 km/h
        if self.tramo == 0 and self.pos > 21000:
            self.tramo = 1
            self.desiredvel = self.carril.max_velocity_t2 # La velocidad máxima a la que desea ir una persona
        lanechange, nuevo_atras = self.lane_change()
        if lanechange:
            self.carril.eliminar(self.id)
            nuevo_adelante = nuevo_atras.adelante
            nuevo_atras.adelante = self
            nuevo_adelante.atras = self
            self.atras = nuevo_atras
            self.adelante = nuevo_adelante
            aux_carril = self.otro_carril
            self.otro_carril = self.carril
            self.carril = aux_carril
 
        gamma=4
        if self.adelante != None:
            self.desiredst = self.mindst + max(0, (self.vel*self.time_hdw + (self.vel-self.adelante.vel)/2*(self.max_acl*self.max_dacl)**0.5))
        if self.choque != 1:
            self.nextpos = self.pos + self.vel*self.dt +1/2*self.acl*self.dt**2
            self.nextvel = max(0, self.vel + (self.acl)*self.dt)
        self.nextacl = max(-self.max_dacl,min(self.max_acl,self.max_acl*(1-(self.vel/self.desiredvel)**gamma - (self.desiredst/(self.gap))**2 )))


    def update(self):
        self.pos = self.nextpos
        self.acl = self.nextacl
        self.vel = self.nextvel
        if self.adelante != None:
            self.gap = self.adelante.pos - self.pos - 4
        self.radar_approaching()
        self.radar_just_passed()

    #TODO EL CONTENIDO DE ESTA FUNCION REFIERE AL MODELO MOBIL, VER SLIDES
    def lane_change(self): 
        if(self.cooldownLC > 0):
            self.cooldownLC -= 1
            return False, False

        if(self.adelante == None or self.atras == None):
            return False, False

        nuevo_atras, nuevo_adelante = self.otro_carril.query(self.pos)
        if nuevo_atras == False or nuevo_adelante == False:
            return False, False

        gamma=4
        newatras_gap = self.pos - nuevo_atras.pos - 4
        newatras_desiredst = nuevo_atras.mindst + max(0, (nuevo_atras.vel*nuevo_atras.time_hdw + (nuevo_atras.vel-self.vel)/2*(nuevo_atras.max_acl*nuevo_atras.max_dacl)**0.5))
        newatras_after = max(-nuevo_atras.max_dacl,min(nuevo_atras.max_acl,nuevo_atras.max_acl*(1-(nuevo_atras.vel/nuevo_atras.desiredvel)**gamma - (newatras_desiredst/(newatras_gap))**2)))
        if newatras_after <= -nuevo_atras.max_dacl :
            return False, False

        self_gap = nuevo_adelante.pos - self.pos - 4
        self_desiredst = self.mindst + max(0, (self.vel*self.time_hdw + (self.vel-nuevo_adelante.vel)/2*(self.max_acl*self.max_dacl)**0.5))
        self_after = max(-self.max_dacl,min(self.max_acl,self.max_acl*(1-(self.vel/self.desiredvel)**gamma - (self_desiredst/(self_gap))**2)))

        self_now = max(-self.max_dacl,min(self.max_acl,self.max_acl*(1-(self.vel/self.desiredvel)**gamma - (self.desiredst/(self.gap))**2)))

        newatras_gap = nuevo_atras.adelante.pos - nuevo_atras.pos - 4
        newatras_desiredst = nuevo_atras.mindst + max(0, (nuevo_atras.vel*nuevo_atras.time_hdw + (nuevo_atras.vel-nuevo_atras.adelante.vel)/2*(nuevo_atras.max_acl*nuevo_atras.max_dacl)**0.5))
        newatras_now = max(-nuevo_atras.max_dacl,min(nuevo_atras.max_acl,nuevo_atras.max_acl*(1-(nuevo_atras.vel/nuevo_atras.desiredvel)**gamma - (newatras_desiredst/(newatras_gap))**2)))

        p = 1
        a_thr = 0.2
        if self.carril.carril == 2:
            atras_gap = self.pos - self.atras.pos - 4
            atras_desiredst = self.atras.mindst + max(0, (self.atras.vel*self.atras.time_hdw + (self.atras.vel-self.vel)/2*(self.atras.max_acl*self.atras.max_dacl)**0.5))
            atras_now = max(-self.atras.max_dacl,min(self.atras.max_acl,self.atras.max_acl*(1-(self.atras.vel/self.atras.desiredvel)**gamma - (atras_desiredst/(atras_gap))**2)))

            atras_gap = self.adelante.pos - self.atras.pos - 4
            atras_desiredst = self.atras.mindst + max(0, (self.atras.vel*self.atras.time_hdw + (self.atras.vel-self.adelante.vel)/2*(self.atras.max_acl*self.atras.max_dacl)**0.5))
            atras_after =  max(-self.atras.max_dacl,min(self.atras.max_acl,self.atras.max_acl*(1-(self.atras.vel/self.atras.desiredvel)**gamma - (atras_desiredst/(atras_gap))**2)))

            if self_after - self_now > p*(atras_now + newatras_now - atras_after - newatras_after) + a_thr :
                self.cooldownLC = 3
                self.color="g"
                return True, nuevo_atras
            else:
                return False, False
        else:
            if self_after - self_now > p*(newatras_now - newatras_after) + a_thr :
                self.color="g"
                self.cooldownLC = 3
                return True, nuevo_atras
            else:
                return False, False
    
    def radar_approaching(self):
        if (1700 <= self.pos < 1800) or (14150 <= self.pos < 14200) or (19950 <= self.pos < 20000):
            if self.vel > self.carril.max_velocity_t1:
                self.desiredvel = self.carril.max_velocity_t1
        elif self.pos<21000:
            self.desiredvel = self.carril.max_velocity_t1
        else:
            self.desiredvel = self.carril.max_velocity_t2

    def radar_just_passed(self):
        aux_multa = 0
        if (1800 <= self.pos < 1820) or (14200 <= self.pos < 14220) or (20000 <= self.pos < 20020):
            if self.vel > self.carril.max_velocity_t1 :
                if self.vel < self.carril.max_velocity_t1 - 40:
                    aux_multa = 150*102.92
                elif (self.vel > self.carril.max_velocity_t1 - 40) and (self.vel < 38.8889) :
                    aux_multa = 250*102.92
                else :
                    aux_multa = 400*102.92
                self.multa += aux_multa
                self.carril.sdc_multados += 1
                self.carril.recaudacion += aux_multa