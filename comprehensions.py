# list comprehension - creates a new list based on values of existing list
# syntax: [<expression>: for item in iterable <condition>]

player_details = [
    ("Jan", 22),
    ("Han", 122),
    ("Pan", 120),
    ("Kanner", 98),
]

players = [player[0] for player in player_details]
# print(players)

players = [player[0] for player in player_details if player[1] > 100]
print(players)

# set comprehension
values = {x*2 for x in range(5)}
print(values)

# dictionary comprehension
values = {x: x*2 for x in range(5)}
print(values)
