# -*- coding: cp1252 -*-
import numpy as np

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

# R�nder

# # Oben

# # Unten

# # Links

# # Rechts

# Mitte
