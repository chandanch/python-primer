# dictionary - A collection of key value pairs
# keys within the dictionary must be unique

# Create Dictionary
player_details = {"name": "Chandio", "score": 450, "level": 3}
player_details = dict(name="Chandio", score=450, level=2)

# Access items
# print(player_details["name"])

# Add or update items
player_details["name"] = "channer"
player_details["nickname"] = "Subernnie"

# Iterate over items - obtains only key from the dictionary
for item in player_details:
    print(item)

# items() - returns the key value as tuple, using tuple unpacking we can obtain the key and value
for key, value in player_details.items():
    print(key, value)


