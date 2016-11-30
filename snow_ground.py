# -*- coding: cp1252 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import math
import os


def create_dir(foldername): # create folder if necessary
    if not os.path.exists(foldername): # check if folder does not exist
        os.makedirs(foldername) # creates new folder
    return foldername # returns the name of the folder


def smooth(array, smoothness):
    for x in range(0, len(array)): # For every x-position in array
        for y in range(0, len(array[0])): # For every y-position in array

            # If Corners
            if x==0 and y==0:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/2) * array[x+1,y] + (smoothness/2) * array[x,y+1]
            elif x==0 and y==len(array[0])-1:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/2) * array[x+1,y] + (smoothness/2) * array[x,y-1]
            elif x==len(array)-1 and y==0:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/2) * array[x-1,y] + (smoothness/2) * array[x,y+1]
            elif x==len(array)-1 and y==len(array[0])-1:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/2) * array[x-1,y] + (smoothness/2) * array[x,y-1]

            # If Edges
            elif x==0:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/3) * array[x+1,y] + (smoothness/3) * array[x,y+1] + (smoothness/3) * array[x,y-1]
            elif x==len(array)-1:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/3) * array[x-1,y] + (smoothness/3) * array[x,y+1] + (smoothness/3) * array[x,y-1]
            elif y==0:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/3) * array[x+1,y] + (smoothness/3) * array[x-1,y] + (smoothness/3) * array[x,y+1]
            elif y==len(array[0])-1:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/3) * array[x+1,y] + (smoothness/3) * array[x-1,y] + (smoothness/3) * array[x,y-1]

            # Remainings
            else:
                array[x,y] = (1-smoothness) * array[x,y] + (smoothness/4) * array[x+1,y] + (smoothness/4) * array[x-1,y] + (smoothness/4) * array[x,y+1] + (smoothness/4) * array[x,y-1]

    return array


def show_surface(array, snow, filename=None):
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

    # x axis edge
    values = [0.]
    points = [0.]
    for ix in np.arange(0, width-0.999, 0.1):
        low = int(math.floor(ix))
        high = int(math.ceil(ix))
        p = float(ix - low)
        value = (1. - p) * array[0, low] + p * array[0, high]
        values.extend([value])
        points.extend([ix])
    values.extend([0])
    points.extend([width-1])
    poly = PolyCollection([list(zip(points, values))], facecolors = 'b')
    ax.add_collection3d(poly, zs=0, zdir='y')

    # y axis edge
    values = [0.]
    points = [0.]
    for iy in np.arange(0, height-0.999, 0.1):
        low = int(math.floor(iy))
        high = int(math.ceil(iy))
        p = float(iy - low)
        value = (1. - p) * array[low, height-1] + p * array[high, height-1]
        values.extend([value])
        points.extend([iy])
    values.extend([0])
    points.extend([height-1])
    poly = PolyCollection([list(zip(points, values))], facecolors = ['b'])
    ax.add_collection3d(poly, zs=height-1, zdir='x')

    # Draw Snowflakes
    xs = []
    ys = []
    zs = []
    for ix in range(0, height):
        for iy in range(0, width):
            if snow[ix, iy] > array[ix, iy]:
                xs.extend([ix])
                ys.extend([iy])
                zs.extend([snow[ix, iy]])
    ax.scatter(xs, ys, zs, c='r', marker='o', alpha=0.5)

    # Save or show graphic
    if filename:
        plt.savefig(filename) # Save the figure
    else:
        plt.show() # Show the figure
    plt.close(fig) # Close the figure


def evaluate_snow(snow, array, step=0.05, p=1.0): # Evaluates all snowflakes
    for ix in range(0, height): # For all x-positions in array
        for iy in range(0, width): # For all y-positions in array
            if snow[ix, iy] == 0: # Inactive snowflake
                if p > np.random.rand(): # Random chance of p
                    snow[ix, iy] = 1 # Make snowflake active
            else: # Active snowflake
                snow[ix, iy] -= np.random.rand() * step # Let snowflakes fall
                if snow[ix, iy] < array[ix, iy]: # Snowflake lower than snow
                    snow[ix, iy] = 0 # Make snowflake inactive
                    array[ix, iy] += 0.025 # Increase snow height at position


def save_as_obj(array, filename, scale=50.):

    big_array = np.zeros((array.shape[0]+2, array.shape[1]+2)) # create a new bigger array with 1 more cell in any direction
    big_array[1:1+array.shape[0], 1:1+array.shape[1]] = array # put the input array in the middle of the bigger one

    f = open(filename, 'w') # open the file
    f.write('# Eckpunkte\n') # start of the vertices
    for x in range(0, len(big_array)): # for every x in the bigger array
        for y in range(0, len(big_array[0])): # for every y in the bigger array
            f.write(get_vertex_string(x, y, big_array[x, y], scale)) # write x, y and z position of the vertex into the file

    f.write('s 1\n') # Smooth the faces in the 3d model
    f.write('# Flächen\n') # start of the faces
    f.write(get_triangles_string(len(big_array), len(big_array[0]))) # write all triangles into the file
    f.close() # you can omit in most cases as the destructor will call it


def get_vertex_string(x, y, z, scale = 1.):
    return 'v ' + str(x / scale) + ' ' + str(z) + ' ' + str(y / scale) + '\n'

def get_triangle_string(a, b, c):
    return 'f ' + str(a) + ' ' + str(b) + ' ' + str(c) + '\n'

def get_square_string(a, b, c, d):
    return 'f ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + '\n'

def get_triangles_string(x_max, y_max):
    number_array = np.zeros((x_max, y_max))
    for x in range(0, x_max):
        for y in range(0, y_max):
            number_array[x, y] = x * y_max + y + 1

    #print_array(number_array)

    result = ""
    for x in range(0, x_max-1):
        for y in range(0, y_max-1):
            result += get_triangle_string(number_array[x, y], number_array[x, y+1], number_array[x+1, y])
            result += get_triangle_string(number_array[x+1, y+1], number_array[x+1, y], number_array[x, y+1])

    result += get_triangle_string(number_array[x_max-1, 0], number_array[0, y_max-1], number_array[0, 0])
    result += get_triangle_string(number_array[0, y_max-1], number_array[x_max-1, 0], number_array[x_max-1, y_max-1])

    return result


def print_array(array):
    for i in range(0, len(array)):
        print array[i]


array = np.zeros((100, 100)) # Create empty array
height = len(array) # Height of ground-array (should be 50)
width = len(array[0]) # Width of ground-array (should be 50)
snow = np.random.rand(height, width) # Create randomized array
savedir = create_dir('obj') # Create a folder


counter = 0 # Set counter
while np.average(array) < 1.0: # While snow height is lower than 1

    evaluate_snow(snow, array, 0.05, 0.1) # Evaluate snowflakes

    smooth(array, 0.2) # Smooth the snow

    #show_surface(array, snow, savedir + "/" + str(i).zfill(4) + '.png') # Save to file
    #show_surface(array, snow) # No save, just show

    counter += 1 # Increase counter

    if counter%100==0:
        save_as_obj(array, savedir + '/100_100_' + str(int(np.average(array) * 100)) + '.obj', 200.)
        print str(counter) + '\t' + str(np.average(array))

#save_as_obj(array, savedir + '/test.obj')
