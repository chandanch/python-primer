# Exceptions - Exceptions are bound to occur in an application
# Exceptions can be handled in the application using the try except blocks.
# try block executes all the code enclosed within it
# In event of an exception the control flows to except block where the exception will be handled

try:
    score = int(input("Score: "))
except ValueError as err:
    print("Invalid Input")
    print("Error")

# Using try, except & else - else block will be executed if no exceptions are raised
try:
    score = int(input("Score: "))
except ValueError as err:
    print("Invalid Input")
    print("Error")
else:
    print("Success Valid Input")

# Using try, except, else & finally - finally block will be excecuted regardless of exception is raised or not
try:
    score = int(input("Score: "))
except ValueError as err:
    print("Invalid Input")
    print("Error")
else:
    print("Success Valid Input")
finally:
    print("Cleanup activity")


# Raising exceptions using raise keyword
def calculate_player_factor(scores, level):
    """
        Calculates PF factor
    """
    if (level <= 0 or scores <= 0):
        raise ValueError("Score or level cannot be 0")
    pf = scores/level
    return pf

try:
    factor = calculate_player_factor(120, 0)
except ValueError as error:
    print(error)
