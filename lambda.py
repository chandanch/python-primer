player_details = [
    ("Jan", 22),
    ("Han", 122),
    ("Pan", 120),
    ("Kanner", 98),
]

# lamba functions: Anonymous functions and are written in a single line\
# syntax: lambda <arguments>:<expression>
# Accepts any no. of arguments, the expression always returns a value

player_details.sort(key=lambda item: item[1])

print(player_details)

players = map(lambda player: player[0], player_details)
print(list(players))

game_title = "Age of new Combronton"


def to_upper(title): return title.upper()


print(to_upper(game_title))

# Filter Items
filteredPlayers = filter(lambda player: player[1] > 100, player_details)
print(list(filteredPlayers))
