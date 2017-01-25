# -*- coding: cp1252 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def show_surface(paramarray, filename=None):

    array = paramarray.reshape(width, height)

    # Create x and y grid
    x = np.arange(0, len(array[0]), 1)
    y = np.arange(0, len(array), 1)
    xs, ys = np.meshgrid(x, y)

    fig = plt.figure()

    DPI = fig.get_dpi()
    fig.set_size_inches(1600.0/float(DPI),1200.0/float(DPI))

    ax = Axes3D(fig)
    ax.set_xlim3d(0, 50) # Set min and max of x axis
    ax.set_ylim3d(0, 50) # Set min and max of y axis
    ax.set_zlim3d(0, 1) # Set min and max of z axis
    ax.plot_surface(xs, ys, array, rstride=1, cstride=1, cmap='GnBu', linewidth=0, antialiased=True)

    # Save or show graphic
    if filename:
        plt.savefig(filename) # Save the figure
    else:
        plt.show() # Show the figure
    plt.close(fig) # Close the figure


width = 50
height = 50
array = np.random.rand(width * height)

p = 0.1
newarray = np.array(array, copy=True)

print array
print newarray
newarray[0] = 1
print array
print newarray

for i in range(0, width*height):
    print i
    print array[i]

# Ecken

# # Oben links

# # Oben rechts

# # Unten links

# # Unten rechts

# Ränder

# # Oben

# # Unten

# # Links

# # Rechts

# Mitte

show_surface(array)

