# with statement - Can be used with objects that supports context management protocol
# Context management protocol consists of 2 methods - __enter__ & __exit__
# Using with statement the resources will be automatically released at the end i.e. python calls the __exit()__
try:
    with open('app.py', encoding='utf-8') as file:
        print('File Opened')
        data = file.fileno()
except ValueError as err:
    print(err)
