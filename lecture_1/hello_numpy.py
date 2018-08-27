#!/usr/bin/env python

import numpy as np
import cv2

# Getting started w/ numpy
# https://docs.scipy.org/doc/numpy/user/quickstart.html

""" 
Here we create our first array, let's see which attributes it has:
shape - dimensions of the array
ndim - number of axes
size - N of elements - product of size
dtype
itemsize - the size of the element in bytes
data - actual elements instead of links
"""

arr = np.array([1, 2, 3])
print('Shape', arr.shape)
print('Dimensions', arr.ndim)

# Let's add more dimensions

arr = np.array([[1],
                [2],
                [3]
])

# arr = np.array([[(1, 1, 1)],
                # [(2, 2, 2)],
                # [(3, 3, 3)]
# ])

print('Shape', arr.shape)
print('Dimensions', arr.ndim)


"""
Note how we create array: we always pass a list or nested list as
an argument, we can also use tubples 
"""

arr = np.array(((1,2),(3,4)))
print(arr)

# It might be useful to specify the type of the array elements
arr = np.array([1, 2, 3], dtype=complex) #or dtype = float
print(arr)

# Sometimes we need to create a specific type of matrix

arr = np.zeros((3), dtype=int)
print(arr)

# we can change dimensions
# arr = np.zeros((3,2,3), dtype=int)
# print(arr)

arr = np.ones((2,2))
print(arr)

"""
Empty, unlike zeros, does not set the array values to zero, 
and may therefore be marginally faster. On the other hand, 
it requires the user to manually set all the values in the
array, and should be used with caution.
"""

arr = np.empty((1,20))
print(arr)

# It is possible to create sequences of numbers
# using arange

print(np.arange( 10, 30, 5 ))
# it accepts float arguments
print(np.arange( 0, 2, 0.3 ))


