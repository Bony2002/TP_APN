from Autopista import Autopista
from Auto import Auto
import random
import numpy as np
import matplotlib.pyplot as plt

def decision(probabilidad) :
    return random.random() < probabilidad

t=0
t_max=20
p_entrar=0
Gral_Paz=Autopista()
velmax=23
cars = []
vel_entrada = 20 #np.random.uniform(15.2778,20.833,1).item() # o de 60 70
acl_entrada = 0
new_auto = Auto(vel_entrada,acl_entrada,None,None,velmax,2)
Gral_Paz.append(Auto=new_auto)
Gral_Paz.analisis()
Gral_Paz.actualizacion()
Gral_Paz.analisis()
Gral_Paz.actualizacion()
# Gral_Paz.analisis()
# Gral_Paz.actualizacion()
# Gral_Paz.analisis()
# Gral_Paz.actualizacion()
vel_entrada = 20 #np.random.uniform(15.2778,20.833,1).item() # o de 60 70
new_auto2 = Auto(vel_entrada,acl_entrada,None,None,velmax,2)
Gral_Paz.append(Auto=new_auto2)

while t<t_max:
    # if decision(1):
    #     vel_entrada = np.random.uniform(15.2778,20.833,1).item() # o de 60 70
    #     acl_entrada = 1
    #     new_auto = Auto(vel_entrada,acl_entrada,None,None,velmax,2)
    #     Gral_Paz.append(new_auto)
    #     cars.append(new_auto)

    print(Gral_Paz.primero.vel, Gral_Paz.ultimo.vel)
    print(t)
    print(Gral_Paz.primero.acl, Gral_Paz.ultimo.acl)
    Gral_Paz.analisis()
    Gral_Paz.actualizacion()
    t+=1


def plot_cars(cars):
    plt.clf()
    plt.xlim(0, 25)  # Adjust the x-axis limits as needed
    plt.ylim(-1, 2)   # Adjust the y-axis limits as needed

    # Load a little car image
    car_icon = plt.imread('car_icon.png')  # Replace 'car_icon.png' with your image path

    for car in cars:
        plt.imshow(car_icon, extent=(car.pos - 0.5, car.pos + 0.5, 1 - 0.5, 1 + 0.5))
    
    plt.pause(0.1)

# plt.ion()  # Turn on interactive mode for dynamic plotting
# for _ in range(50):  # Number of time steps
#     Gral_Paz.actualizacion()
#     plot_cars(cars)

# plt.ioff()  # Turn off interactive mode
# plt.show()