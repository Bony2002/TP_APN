from Autopista import Autopista
from Auto import Auto
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def decision(probabilidad) :
    return random.random() < probabilidad

p_entrar=0.7
t_max=200
cooldown=2
id=0
Gral_Paz=Autopista(23,24300,0)
    
fig, ax = plt.subplots()
dots, = ax.plot([], [], 'bo')

def initplot():
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, 2)
    dots.set_data([], [])
    return dots,

def update(frame):
    global cooldown, id, p_entrar, Gral_Paz
    if cooldown>=5 and decision(p_entrar):
        id+=1.0
        cooldown=-1
        if Gral_Paz.ultimo != None and Gral_Paz.ultimo.vel < 15 and Gral_Paz.ultimo.pos < 100:
            vel_entrada = np.random.uniform(Gral_Paz.ultimo.vel-3,Gral_Paz.ultimo.vel,1).item()
        else:
            vel_entrada = np.random.uniform(15.2778,20.833,1).item() # o de 60 70
        vel_entrada = np.random.uniform(15.2778,20.833,1).item() # o de 60 70
        acl_entrada = 0
        new_auto = Auto(id,0,vel_entrada,acl_entrada,23,True)
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
