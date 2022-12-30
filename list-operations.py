names = ["Dan", "Ban", "Kan", "Zan"]

# Add Items to List
# Append() - Adds an item to the end of the list
names.append("Jan")
# insert() - Inserts an item at a specific position in the list
names.insert(1, "Han")
names.insert(0, "---")
# print(names)

# Remove Items from list
# pop() - removes the last item from the list
names.pop()
names.pop(0)
# print(names)

# remove() - removes the first occurrance of the item from the list
names.remove('Zan')

# del - removes an item at the specified position of the list
del names[2]
del names[0:2]

# clear() - removes all items from the list - resets to empty list
names.clear()


# Finding item(s) in list
player_events = ['Game Created', 'Live Mode Entered',
                 'Stealth', 'Covert', 'Escaped']

# index() - returns the index of the specified item of the list
# print(player_events.index("Stealth"))

# count() - returns the no. of occurrances of a given item in the list
# print(player_events.count("Covert"))

# list.sort() - sorts the items in the list.
player_scores = [1, 89, 34, 23, 12, 100, 98]
player_scores.sort()
print(player_scores)

player_details = [
    ("Jan", 22),
    ("Han", 122),
    ("Pan", 120),
    ("Kanner", 98),
]


def sort_player(player):
    return player[1]


player_details.sort(key=sort_player)

print(player_details)
