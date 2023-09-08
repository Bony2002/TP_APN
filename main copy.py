from Autopista import Autopista
from Auto import Auto
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def decision(probabilidad) :
    return random.random() < probabilidad

t_max=3000
cooldown=2
id=0
Gral_Paz=Autopista(23,24300,0)

for i in range(t_max):
    if cooldown>=5 and decision(Gral_Paz.p_entrar) :
        id+=1.0
        cooldown=-1
        if Gral_Paz.ultimo != None and Gral_Paz.ultimo.vel < 15 and Gral_Paz.ultimo.pos < 100:
            vel_entrada = np.random.uniform(Gral_Paz.ultimo.vel-3,Gral_Paz.ultimo.vel,1).item()
        else:
            vel_entrada = np.random.uniform(15.2778,20.833,1).item() # o de 60 70
        acl_entrada = 0
        new_auto = Auto(id,0,vel_entrada,acl_entrada,23,True)
        Gral_Paz.append(new_auto)           
    cooldown+=1
    Gral_Paz.revision()
    Gral_Paz.analisis()
    positions = Gral_Paz.actualizacion()
    