from array import array

# Array - An array contains a collection of similar items
# All the elements in the array must of similar type.
viscosity_indexes = array('f', [12.3, 23.12, 90.12, 11.34])

viscosity_indexes.insert(1, 0.2)

print(viscosity_indexes)
