import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create an array of initial positions for the dots
num_dots = 10
initial_positions = np.random.rand(num_dots) * 2 * np.pi  # Random initial positions

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Create a scatter plot with the initial positions
dots, = ax.plot(initial_positions, initial_positions**0, 'bo')

# Function to update the dot positions at each time step
def update(frame):
    # Update the positions of the dots (for example, by adding a small increment)
    new_positions = initial_positions + frame * 0.1
    # Update the dot data with the new positions
    dots.set_xdata(new_positions)
    dots.set_ydata(new_positions**0)
    return dots,

# Create an animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True)

# Display the animation
plt.show()

