def show_player_details():
    """
        Show Player information to the user
    """
    print("Player Name: Chandio")
    print("Player Score: 45")


show_player_details()


def calculate_bonus(score, level):
    """
        Calculates bonus based on score & level
    """
    bonus = (score * 1.3) + (level * 2)
    return bonus


print(f"Bonus Recieved: {calculate_bonus(12, 4)}")

# Keyword & Default arguments


def calculate_rewards(score, level, rating=2):
    """
        Calculates rewards based on the score and level,
        rating is optional here
    """
    return (score * 3) + (level + 2) + rating


print(f"Reward Obtained: {calculate_rewards(score=123, level=1)}")

# *args: accept any no. of arguments


def calculate_total_score(*scores):
    """
        Calculates total score based on the score values passed
    """
    total_score = 0
    for score in scores:
        total_score += score
    return total_score


print(calculate_total_score(12, 123, 120))

# **args: accepts any number of keyword arguments
# creates a dictionary using the keyword argument name and value


def save_user(**user):
    """
        Prints user details on the list; and maps -> to the details. To the new details that are part
    """
    print(user)


save_user(id=1, name='chandio', loc='KAN')
