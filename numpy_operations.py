"""
NumPy is used when working with large multi-dimensional arrays
Numpy creates an array object known as ndarray.
ndarray has methods that makes working with large multi-dimensional arrays easier

NumPy is 50x faster than python lists. The NumPy arrays are stored in contigious place in memory
Hence it makes it easier for processes to access and manipulate the NumPy array efficiently

Storing an array in an continious place in memory is known as locality of reference
"""

# create an numpy array

import numpy as np

arr = np.array([100, 456, 89, 102])
print(arr)

# Accessing elements of an array
print(arr[1])

# Creating an 2D array
arr2d = np.array([[12, 23, 34], [233, 239, 292]])

# Returns the total no. of rows and columns of an array
print(arr2d.shape)

random_arr = np.random.random((3))

for arr in random_arr:
    print(arr)

print(list([1, 3, 4, 5]))

# Get sum of an array 
arr = np.array([100, 456, 89, 102])
print(np.sum(arr))

# Manipulate array
arr = np.array([100, 456, 89, 102]) * 100

print(arr)
