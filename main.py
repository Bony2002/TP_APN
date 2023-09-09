from Autopista import Autopista
from Auto import Auto
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

    # VARIABLES GLOBALES
p_entrar=0.7
t_max=2000
cooldown=2
id=0
Gral_Paz=Autopista(23,24300,0)

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
    global cooldown, id, p_entrar, Gral_Paz
    if (cooldown >= 3) and (random.random() < p_entrar):
        id+=1.0
        cooldown=-1
        if (Gral_Paz.ultimo.pos > 10 if Gral_Paz.ultimo != None else True):
            if Gral_Paz.ultimo != None and Gral_Paz.ultimo.vel < 15 and Gral_Paz.ultimo.pos < 100:
                vel_entrada = np.random.normal(Gral_Paz.ultimo.vel-1.5, 1) # si la autopista está muy cargada es esta la uniforme
            else:
                vel_entrada = np.random.normal(18.0554, 1.5) # Normal para ver la velocidad de entrada
            acl_entrada = 0
            new_auto = Auto(id,0,vel_entrada,acl_entrada,True)
            Gral_Paz.append(new_auto)
    cooldown+=1
    Gral_Paz.revision()
    Gral_Paz.analisis()
    positions = Gral_Paz.actualizacion()
    dots.set_data(positions, np.ones(len(positions)))
    dots.set_ydata(np.ones(len(positions)))
    return dots,

ani = FuncAnimation(fig, update, init_func=initplot, frames=range(t_max), blit=True)
plt.show()

#loaded_df = pd.read_csv('TP_APN/resumen.csv')
