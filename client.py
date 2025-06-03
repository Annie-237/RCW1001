import requests 
#url = 'http://localhost:8000'
url = 'https://appi-ghfwdsbkd8a2d7cj.canadaeast-01.azurewebsites.net'

response = requests.get(url)
response = response.json()
print(response['message'])