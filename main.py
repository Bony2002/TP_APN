from Autopista import Autopista
from Auto import Auto
import random
import numpy as np

def decision(probabilidad) :
    return random.random() < probabilidad

t=0
t_max=10
p_entrar=0
Gral_Paz=Autopista()
velmax=80

while t<t_max:
    if decision(p_entrar):
        vel_entrada = np.random.uniform(55,75,1).item()
        acl_entrada = np.random.uniform(0,10,1).item()
        new_auto = Auto(vel_entrada,acl_entrada,velmax)
        Gral_Paz.append(Auto=new_auto)
    Gral_Paz.analisis()
    Gral_Paz.actualizacion()
    t+=1