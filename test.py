import requests

url = 'http://160.16.140.103/api/point'
data = {'prefecture': ''}

print("Hallo")

response = requests.post(url, data=data)
print(response.text)
