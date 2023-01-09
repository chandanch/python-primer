import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=800)

print(response)