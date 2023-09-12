from Autopista import Autopista
from Auto import Auto
from SDC import SDC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import sys
import signal

# Define a signal handler
def signal_handler(sig, frame):

    df = pd.DataFrame(data)
    file_name="data.csv"
    df.to_csv(file_name, index=False)

    sys.exit(0)

# Attach the signal handler
signal.signal(signal.SIGINT, signal_handler)


####################################################################################

def crear_autopista_y_simular(p,t_max,sdc,p_sdc,data):

        # VARIABLES DE SDC
    intro_SDC = sdc
    p_SDC = p_sdc
    tiempos_terminacion_SDC = []
    datos_choques_SDC = []
    sdc_cars = 0

    t_inc=2300
    cooldown1=2
    cooldown2=2
    iden=0
    Gral_Paz_1=Autopista(23,24300,0,1)
    Gral_Paz_2=Autopista(23,24300,0,2)
    tiempos_terminacion = []
    datos_choques = []
    cars = 0
        
    for t in range(t_inc):

        # INTRODUCCIÓN DE AUTOS AL PRIMER CARRIL

        if (cooldown1 >= 4) and (np.random.uniform(0,1) < p):
            iden+=1.0
            cooldown1=-1
            if (Gral_Paz_1.ultimo.pos > 30 if Gral_Paz_1.ultimo != None else True):
                if Gral_Paz_1.ultimo != None and Gral_Paz_1.ultimo.vel < 15 and Gral_Paz_1.ultimo.pos < 100:
                    vel_entrada = np.random.normal(Gral_Paz_1.ultimo.vel-3, 1) # si la autopista está muy cargada es esta la uniforme
                else:
                    vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
                acl_entrada = 0

                # INTRODUCCION DEL SDC

                if intro_SDC and (np.random.uniform(0,1) < p_SDC):
                    new_auto = SDC(iden,t,0,vel_entrada,acl_entrada,Gral_Paz_1,Gral_Paz_2)
                    sdc_cars+=1
                else :
                    new_auto = Auto(iden,t,0,vel_entrada,acl_entrada,Gral_Paz_1,Gral_Paz_2)
                    cars+=1
                Gral_Paz_1.append(new_auto)

        # INTRODUCCIÓN DE AUTOS AL SEGUNDO CARRIL

        if (cooldown2 >= 4) and (np.random.uniform(0,1) < p):
            cooldown2 = -1
            if (Gral_Paz_2.ultimo.pos > 30 if Gral_Paz_2.ultimo != None else True):
                if Gral_Paz_2.ultimo != None and Gral_Paz_2.ultimo.vel < 15 and Gral_Paz_2.ultimo.pos < 100:
                    vel_entrada = np.random.normal(Gral_Paz_2.ultimo.vel-1.5, 1) # si la autopista está muy cargada es esta la uniforme
                else:
                    vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
                acl_entrada = 0
                iden+=1
                
                # INTRODUCCION DEL SDC

                if intro_SDC and (np.random.uniform(0,1) < p_SDC):
                    new_auto = SDC(iden,t,0,vel_entrada,acl_entrada,Gral_Paz_2,Gral_Paz_1)
                    sdc_cars+=1
                else :
                    new_auto = Auto(iden,t,0,vel_entrada,acl_entrada,Gral_Paz_2,Gral_Paz_1)
                    cars+=1
                Gral_Paz_2.append(new_auto)

        
        cooldown1+=1
        cooldown2+=2
    cooldown1=2
    cooldown2=2
    print("termino la iniciacion")
    ########################################################### INICIACION DE LA AUTOPISTA 

    for t in range(t_max):

        # INTRODUCCIÓN DE AUTOS AL PRIMER CARRIL

        if (cooldown1 >= 4) and (np.random.uniform(0,1) < p):
            iden+=1.0
            cooldown1=-1
            if (Gral_Paz_1.ultimo.pos > 30 if Gral_Paz_1.ultimo != None else True):
                if Gral_Paz_1.ultimo != None and Gral_Paz_1.ultimo.vel < 15 and Gral_Paz_1.ultimo.pos < 100:
                    vel_entrada = np.random.normal(Gral_Paz_1.ultimo.vel-3, 1) # si la autopista está muy cargada es esta la uniforme
                else:
                    vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
                acl_entrada = 0

                # INTRODUCCION DEL SDC

                if intro_SDC and (np.random.uniform(0,1) < p_SDC):
                    new_auto = SDC(iden,t,0,vel_entrada,acl_entrada,Gral_Paz_1,Gral_Paz_2)
                    sdc_cars+=1
                else :
                    new_auto = Auto(iden,t,0,vel_entrada,acl_entrada,Gral_Paz_1,Gral_Paz_2)
                    cars+=1
                Gral_Paz_1.append(new_auto)

        # INTRODUCCIÓN DE AUTOS AL SEGUNDO CARRIL

        if (cooldown2 >= 4) and (np.random.uniform(0,1) < p):
            cooldown2 = -1
            if (Gral_Paz_2.ultimo.pos > 30 if Gral_Paz_2.ultimo != None else True):
                if Gral_Paz_2.ultimo != None and Gral_Paz_2.ultimo.vel < 15 and Gral_Paz_2.ultimo.pos < 100:
                    vel_entrada = np.random.normal(Gral_Paz_2.ultimo.vel-1.5, 1) # si la autopista está muy cargada es esta la uniforme
                else:
                    vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
                acl_entrada = 0
                iden+=1
                
                # INTRODUCCION DEL SDC

                if intro_SDC and (np.random.uniform(0,1) < p_SDC):
                    new_auto = SDC(iden,t,0,vel_entrada,acl_entrada,Gral_Paz_2,Gral_Paz_1)
                    sdc_cars+=1
                else :
                    new_auto = Auto(iden,t,0,vel_entrada,acl_entrada,Gral_Paz_2,Gral_Paz_1)
                    cars+=1
                Gral_Paz_2.append(new_auto)

        
        cooldown1+=1
        cooldown2+=2
        tiempos1,choques1 = Gral_Paz_1.revision(t)
        tiempos2,choques2 = Gral_Paz_2.revision(t)
        tiempos_terminacion = tiempos_terminacion + tiempos1[0]
        tiempos_terminacion = tiempos_terminacion + tiempos2[0]
        datos_choques = datos_choques + choques1[0]
        datos_choques = datos_choques + choques2[0]

        if intro_SDC:
            tiempos_terminacion_SDC = tiempos_terminacion_SDC + tiempos1[1]
            tiempos_terminacion_SDC = tiempos_terminacion_SDC + tiempos2[1]
            datos_choques_SDC = datos_choques_SDC + choques1[1]
            datos_choques_SDC = datos_choques_SDC + choques2[1]


        Gral_Paz_1.analisis()
        Gral_Paz_2.analisis()
        positions1,carril1,colores1 = Gral_Paz_1.actualizacion()
        positions2,carril2,colores2 = Gral_Paz_2.actualizacion()
    # print(np.array(tiempos_terminacion).mean())
    # plt.hist(tiempos_terminacion)
    # plt.show()
    # print(len(datos_choques))
    # print(len(datos_choques)/cars)    
    data["cantidad_de_autos"].append(Gral_Paz_1.cant_autos + Gral_Paz_2.cant_autos)
    data["cantidad_de_autos_multados"].append(Gral_Paz_1.cant_multados + Gral_Paz_2.cant_multados)
    data["recaudacion"].append(Gral_Paz_1.recaudacion + Gral_Paz_2.recaudacion)
    data["total_tiempos"].append(tiempos_terminacion)
    data["datos_choques"].append(datos_choques)
    data["total_tiempos_sdc"].append(tiempos_terminacion_SDC)
    data["total_choques_sdc"].append(datos_choques_SDC)
    return

###########################################################

data = {
    "horas": [],
    "cantidad_de_autos":[],
    "cantidad_de_autos_multados":[],
    "recaudacion":[],
    "prob_entrar": [],
    "total_tiempos": [],
    "datos_choques": [],
    "sdc": [],
    "prop_sdc":[],
    "total_tiempos_sdc": [],
    "total_choques_sdc": []
}


#seeds = [44262256,44362396,44755006]
horas = [2,5,7]
p_entrar=[0.2,0.4,0.6]
sdc = [False,True]
p_sdc = [0.3,0.8]

for hr in horas:
    for p in p_entrar:
        for hay_sdc in sdc:
            if hay_sdc==True:
                for p_s in p_sdc:
                    np.random.seed(256396006)
                    t_max=7200*hr
                    crear_autopista_y_simular(p,t_max,hay_sdc,p_s,data)
                    data["horas"].append(hr)
                    data["prob_entrar"].append(p)
                    data["sdc"].append(hay_sdc)
                    data["prop_sdc"].append(p_s)
                    print("La fila:",hr,p,hay_sdc,p_s,"está lista")
            else:
                np.random.seed(256396006)
                t_max=7200*hr
                crear_autopista_y_simular(p,t_max,hay_sdc,0,data)
                data["horas"].append(hr)
                data["prob_entrar"].append(p)
                data["sdc"].append(hay_sdc)
                data["prop_sdc"].append(None)
                print("La fila:",hr,p,hay_sdc,None,"está lista")


df = pd.DataFrame(data)
file_name="data.csv"
df.to_csv(file_name, index=False)