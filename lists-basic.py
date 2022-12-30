level1_scores = [3, 12, 4, 64]

level2_scores = [45, 66, 32]

# Combine lists
combined_scores = level1_scores + level2_scores
# print(combined_scores)

# Repeat Items in list
repeated = ["*"] * 10
# print(repeated)

# slicing list - <list_name>[start: stop]
player_scores = list(range(1, 21))
# print(player_scores)
# print(player_scores[2:8])

# step through items - <list_name>[::step_value]
# print(player_scores[::-1])

# list unpacking
player_details = ['Chandio', 'Striker', 234]
name, nick_name, score = player_details
# print(name, nick_name, score)

# unpacking and packing the remaing items to list using *
first_score, *other_scores = player_scores
# print(first_score, other_scores)

first_score, *other_scores, last_score = player_scores
# print(first_score, last_score)

# Using enumurate() to enumurate over the list - Returns a tuple with index and the item
# enumerate() returns an enumerate object, this object is iterable and returns a tuple in each iteration
player_events = ['Game Created', 'Live Mode Entered',
                 'Stealth', 'Covert', 'Escaped']
# using tuple unpacking to get index and item
for index, event in enumerate(player_events):
    print(index, event)
