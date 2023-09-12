from Autopista import Autopista
from Auto import Auto
from SDC import SDC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


np.random.seed(44262256)

    # VARIABLES DE SDC
intro_SDC = False
p_SDC = 0.9
tiempos_terminacion_SDC = []
datos_choques_SDC = []
sdc_cars = 0
####################################################################################

def crear_autopista_y_simular(p,t_max):
    t_inc=2 
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
    # if intro_SDC:
    #     print(np.array(tiempos_terminacion_SDC).mean())
    #     print(len(datos_choques_SDC))
    #     print(len(datos_choques_SDC)/sdc_cars) 
    return tiempos_terminacion,datos_choques

###########################################################

    # VARIABLES GLOBALES
#Probabilidades a probar 0.2 - 0.4 - 0.5 (Más de 0.5 la cantidad de choques es excesiva)

p_entrar=[0.1,0.3,0.5,0.7]
t_max=7200*2 # 1 hr : 7200
total_tiempos=[]
total_choques=[]
for i in p_entrar:
    tiempos,choques=crear_autopista_y_simular(i,t_max)
    total_tiempos.append(tiempos)
    total_choques.append(choques)
 

dfC=pd.DataFrame(total_choques)
dfT=pd.DataFrame(total_tiempos)
fileT="/TP_APN/graficos/tiempos3.csv"
fileC="/TP_APN/graficos/choques3.csv"
dfT.to_csv(fileT,index=False)
dfC.to_csv(fileC,index=False)
########################################################### INICIACION DE LA AUTOPISTA 
