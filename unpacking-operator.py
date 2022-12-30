# unpacking operator - Takes the items from the iterable and unpacks or spreads them into a container. This container can be another iterable

# unpacking with list - use *
level1_scores = [23, 13, 13]
level2_scores = [211, 33, 44]
combined_scores = [*level1_scores, 34, 455, *level2_scores]
print(combined_scores)

# unpacking with dictionary - use **
player_details = dict(name="chandio", bio="dheesd", fame=23)
player_score = dict(level=12, score=1333)
combined_details = {**player_score, **player_details}
print(combined_details)

