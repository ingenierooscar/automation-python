import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '885909950805'}
response = requests.get(baseUrl, params=parameters)
print(response.url)

content = response.content #convert response to Json
info = json.loads(content) #transform Json to Diccionary 
print(type(info))
print(info)

#checing diccionary
item = info['items']
itemInfo = item[0]
titele = itemInfo['title']
brando = itemInfo['brand']

print(titele)
print(brando)