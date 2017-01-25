# -*- coding: cp1252 -*-
import numpy as np

width = 50
height = 50
array = np.random.rand(width * height)

p = 0.1
newarray = np.array(array, copy=True)
