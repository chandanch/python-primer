# create an tuple
points = (1, 2, 3, 4)
# alternative way
points = 1, 2, 3, 4, 5

# Accessing tuple items
print(points[0])

# obtain a range of items
print(points[0:2])

# Check if item exists in tuple
print(f"{'Exists' if 4 in points else 'Not Found'}")

# Tuple unpacking
name, age, score = ('Chandio', 12, 450)
print(name, age, score)
