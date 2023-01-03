"""
    Modules helps to organize code, it helps to keep related code in terms of
    methods, classes etc in a single file
"""

# importing moduules and specific objects from module
from rewards_calculator import calculate_bonus, calculate_rewards
from game import create_game

# importing all objects from the module
# import rewards_calculator

calculate_rewards(133)

print(calculate_bonus(122, 2))

create_game()