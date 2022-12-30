# set - A set is an collection of unique items
# duplicates are not allowed in the set and cannot be accessed using indexes since its unordered
# Create
scores = {22, 34, 78}
# Add a new item
scores.add(233)
scores.add(569)
# Remove an item
scores.remove(569)

# Sets are usual in mathematical comparisions - Union(|), Intersection(&) Symmetry (^) Difference (-)
new_scores = {11, 34, 78, 79}
print(scores & new_scores)
