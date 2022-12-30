# zip() - combines multiple lists as a tuple and returns a zip object

levels = [1, 2, 3]
scores = [34, 44, 98]

combined_data = zip(levels, scores)

print(list(combined_data))