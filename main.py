from Autopista import Autopista
from Auto import Auto
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def decision(probabilidad) :
    return random.random() < probabilidad


p_entrar=0.7
t_max=200
cooldown=2
id=0
Gral_Paz=Autopista(23,24300,0)

for i in range(t_max):
    if cooldown>=5 and decision(p_entrar) :
        id+=1.0
        cooldown=-1
        vel_entrada = np.random.uniform(15.2778,20.833,1).item() # o de 60 70
        acl_entrada = 0
        new_auto = Auto(id,0,vel_entrada,acl_entrada,23,True)
        Gral_Paz.append(new_auto)
        if i == 1 :
            resumen=pd.DataFrame(Gral_Paz.resumen())
            resumen.to_csv('resumen.csv', index=False)            
    cooldown+=1
    Gral_Paz.revision()
    Gral_Paz.analisis()
    Gral_Paz.actualizacion()

# resumen=pd.DataFrame(Gral_Paz.resumen())
# resumen.to_csv('resumen.csv', index=False)

#loaded_df = pd.read_csv('TP_APN/resumen.csv')



# def plot_cars(cars):
#     plt.clf()
#     plt.xlim(0, 25)  # Adjust the x-axis limits as needed
#     plt.ylim(-1, 2)   # Adjust the y-axis limits as needed

#     # Load a little car image
#     car_icon = plt.imread('car_icon.png')  # Replace 'car_icon.png' with your image path

#     for car in cars:
#         plt.imshow(car_icon, extent=(car.pos - 0.5, car.pos + 0.5, 1 - 0.5, 1 + 0.5))
    
#     plt.pause(0.1)

# # plt.ion()  # Turn on interactive mode for dynamic plotting
# # for _ in range(50):  # Number of time steps
# #     Gral_Paz.actualizacion()
# #     plot_cars(cars)

# # plt.ioff()  # Turn off interactive mode
# # plt.show()