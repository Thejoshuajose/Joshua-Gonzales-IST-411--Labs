#Project: Solo Lab Python3 and CURL urllib
#Purpose Details: Use CURL tool to extract payload from the internet
#Course: IST411
#Author: Joshua Gonzales
#Date Developed: 9/13/2024
#Last Changed: 9/13/2024
#Rev: 2


import json
import urllib.request

websiteResponse = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts/1/comments')

payload = websiteResponse.read()

payloadJSON = json.loads(payload.decode('utf-8'))

with open('curl.json' , 'w') as json_file:
	json.dump(payloadJSON, json_file)

with open('curl.json','r') as json_file:
	data = json.load(json_file)

print(json.dumps(data))
