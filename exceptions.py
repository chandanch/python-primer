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
