from Autopista import Autopista
from Auto import Auto
from SDC import SDC
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

    # VARIABLES DE SDC
intro_SDC = True
p_SDC = 0.5

    # VARIABLES GLOBALES
p_entrar=0.5
t_max=3000
cooldown1=2
cooldown2=2
iden=0
Gral_Paz_1=Autopista(23,24300,0,1)
Gral_Paz_2=Autopista(23,24300,0,2)
contador=0
dots = None

    # INICIALIZACION DEL PLOT
fig, ax = plt.subplots(figsize=(10, 4))
#dots, = ax.plot([], [], 'bo')

def initplot():
    global dots
    ax.set_xlim(0, 4000)
    ax.set_ylim(0.5, 2.5)
    #dots.set_data([], [])
    dots = ax.scatter([], [], c='b', marker='o', s=20)
    return dots,

dots = ax.scatter([], [], c='b', marker='o', s=20) 

    # MAIN
def update(frame):
    global cooldown1, cooldown2, iden, p_entrar, Gral_Paz_1, Gral_Paz_2, contador, dots
    if (cooldown1 >= 3) and (np.random.uniform(0,1) < p_entrar):
        
        cooldown1=-1
        if (Gral_Paz_1.ultimo.pos > 10 if Gral_Paz_1.ultimo != None else True):
            if Gral_Paz_1.ultimo != None and Gral_Paz_1.ultimo.vel < 15 and Gral_Paz_1.ultimo.pos < 100:
                vel_entrada = np.random.normal(Gral_Paz_1.ultimo.vel-1.5, 1) # si la autopista está muy cargada es esta la uniforme
            else:
                vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
            acl_entrada = 0
            iden+=1
            # INTRODUCCION DEL SDC

            if intro_SDC and (np.random.uniform(0,1) < p_SDC):
                new_auto = SDC(iden,contador,0,vel_entrada,acl_entrada,Gral_Paz_1,Gral_Paz_2)
            else :
                new_auto = Auto(iden,contador,0,vel_entrada,acl_entrada,Gral_Paz_1,Gral_Paz_2)
            Gral_Paz_1.append(new_auto)

    # INTRODUCCIÓN DE AUTOS AL SEGUNDO CARRIL

    if (cooldown2 >= 3) and (np.random.uniform(0,1) < p_entrar):
        cooldown2 = -1
        if (Gral_Paz_2.ultimo.pos > 10 if Gral_Paz_2.ultimo != None else True):
            if Gral_Paz_2.ultimo != None and Gral_Paz_2.ultimo.vel < 15 and Gral_Paz_2.ultimo.pos < 100:
                vel_entrada = np.random.normal(Gral_Paz_2.ultimo.vel-1.5, 1) # si la autopista está muy cargada es esta la uniforme
            else:
                vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
            acl_entrada = 0
            iden+=1

            # INTRODUCCION DEL SDC

            if intro_SDC and (np.random.uniform(0,1) < p_SDC):
                new_auto = SDC(iden,contador,0,vel_entrada,acl_entrada,Gral_Paz_2,Gral_Paz_1)
            else :
                new_auto = Auto(iden,contador,0,vel_entrada,acl_entrada,Gral_Paz_2,Gral_Paz_1)
            Gral_Paz_2.append(new_auto)

    cooldown1+=1
    cooldown2+=2

    Gral_Paz_1.analisis()
    Gral_Paz_2.analisis()
    positions1,carril1,colors1 = Gral_Paz_1.actualizacion()
    positions2,carril2,colors2 = Gral_Paz_2.actualizacion()

    positions = positions1 + positions2
    carriles = carril1 + carril2
    colors = colors1 + colors2
    #dots.set_data(positions, carriles)
    #dots.set_ydata(carriles)
    #dots.set_offsets(np.column_stack((positions, carriles)))
    #dots.set_facecolor(colors)
    dots.remove()
    dots = ax.scatter(positions, carriles, marker='o', s=40, c=colors)

    contador += 1
    if contador >= t_max:
        ani.event_source.stop()
    return dots,


ani = FuncAnimation(fig, update, init_func=initplot, frames=range(t_max), blit=True)
plt.show()