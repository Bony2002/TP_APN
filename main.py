from Autopista import Autopista
from Auto import Auto
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

    # VARIABLES GLOBALES
p_entrar=np.random.normal(0.2,0.1)
t_max=2000
cooldown1=2
cooldown2=2
id=0
Gral_Paz_1=Autopista(23,24300,0,1)
Gral_Paz_2=Autopista(23,24300,0,2)


    # INICIALIZACION DEL PLOT
fig, ax = plt.subplots(figsize=(10, 4))
dots, = ax.plot([], [], 'bo')

def initplot():
    ax.set_xlim(0, 2000)
    ax.set_ylim(0.5, 2.5)
    dots.set_data([], [])
    return dots,

    # MAIN
def update(frame):
    global cooldown1, cooldown2, id, p_entrar, Gral_Paz_1, Gral_Paz_2
    if (cooldown1 >= 3) and (np.random.uniform(0,1) < p_entrar):
        id+=1.0
        cooldown1=-1
        if (Gral_Paz_1.ultimo.pos > 10 if Gral_Paz_1.ultimo != None else True):
            if Gral_Paz_1.ultimo != None and Gral_Paz_1.ultimo.vel < 15 and Gral_Paz_1.ultimo.pos < 100:
                vel_entrada = np.random.normal(Gral_Paz_1.ultimo.vel-1.5, 1) # si la autopista está muy cargada es esta la uniforme
            else:
                vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
            acl_entrada = 0
            new_auto = Auto(id,0,vel_entrada,acl_entrada,Gral_Paz_1,Gral_Paz_2)
            Gral_Paz_1.append(new_auto)
    if (cooldown2 >= 3) and (np.random.uniform(0,1) < p_entrar):
        id += 1.0
        cooldown2 = -1
        if (Gral_Paz_2.ultimo.pos > 10 if Gral_Paz_2.ultimo != None else True):
            if Gral_Paz_2.ultimo != None and Gral_Paz_2.ultimo.vel < 15 and Gral_Paz_2.ultimo.pos < 100:
                vel_entrada = np.random.normal(Gral_Paz_2.ultimo.vel-1.5, 1) # si la autopista está muy cargada es esta la uniforme
            else:
                vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
            acl_entrada = 0
            new_auto = Auto(id,0,vel_entrada,acl_entrada,Gral_Paz_2,Gral_Paz_1)
            Gral_Paz_2.append(new_auto)
    cooldown1+=1
    cooldown2+=1
    Gral_Paz_1.revision()
    Gral_Paz_2.revision()
    Gral_Paz_1.analisis()
    Gral_Paz_2.analisis()
    positions1,carril1 = Gral_Paz_1.actualizacion()
    positions2,carril2 = Gral_Paz_2.actualizacion()
    positions = positions1 + positions2
    carriles = carril1 + carril2
    #dots.set_data(positions2, np.ones(len(positions2)) + np.ones(len(positions2)) )
    dots.set_data(positions, carriles)
    dots.set_ydata(carriles)
    #dots.set_ydata(np.ones(len(positions2)) + np.ones(len(positions2)))
    return dots,

ani = FuncAnimation(fig, update, init_func=initplot, frames=range(t_max), blit=True)
plt.show()

#loaded_df = pd.read_csv('TP_APN/resumen.csv')
