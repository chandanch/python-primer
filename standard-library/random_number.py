import random
import string

# Generates an randon floating point number between 0 & 1
print(random.random())

# Generate an random number between the range of two numbers specified
print(random.randint(1, 100))

# selects an element randomly from the list
print(random.choice([1, 4, 12, 9, 102]))

# selects the specified no of elements(k arg) randomly from the list
print(random.choices([1, 4, 12, 9, 102], k=2))

# Generating random password using random.choices()
password_characters = ""+ string.ascii_letters + string.digits + string.punctuation
random_password = random.choices(password_characters, k=9)
print("".join(random_password))
