import matplotlib.pyplot as plt
import numpy as np
import random

class Car:
    def __init__(self, x, y, vx):
        self.x = x
        self.y = y
        self.vx = vx

def update_cars(cars):
    for car in cars:
        car.x += car.vx

def plot_cars(cars):
    plt.clf()
    plt.xlim(0, 25)  # Adjust the x-axis limits as needed
    plt.ylim(-1, 2)   # Adjust the y-axis limits as needed

    # Load a little car image
    car_icon = plt.imread('car_icon.png')  # Replace 'car_icon.png' with your image path

    for car in cars:
        plt.imshow(car_icon, extent=(car.x - 0.5, car.x + 0.5, car.y - 0.5, car.y + 0.5))
    
    plt.pause(0.1)

def main():
    num_cars = 15
    cars = [Car(x=random.randint(0, 25), y=random.randint(0, 1), vx=random.uniform(0.1, 2)) for _ in range(num_cars)]

    plt.ion()  # Turn on interactive mode for dynamic plotting

    for _ in range(50):  # Number of time steps
        update_cars(cars)
        plot_cars(cars)

    plt.ioff()  # Turn off interactive mode
    plt.show()

if __name__ == "__main__":
    main()
