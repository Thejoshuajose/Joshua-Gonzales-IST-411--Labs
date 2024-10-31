#Project: Lab 4 MongoDB
#Prupose Details: Learn how to use python 3 to download and save and show it into MongoDB
#Course: IST411
#Author: Joshua Gonzales
#Date Developed: 9/20/24
#Last Date Changed: 9/20/24
#Rev: 1

import json
import urllib.request
from pymongo import MongoClient
import sys

websiteResponse = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts/1/comments')

payload =json.loads(websiteResponse.read())


try:
	client = MongoClient('localhost',27017)
	print("Connected to MongoDB")
	db = client.team2
	print("Got the Databse test_database")
	collection = db.jsonPayloadGonzales
	print("Got the Collection")
	print("Created the Document Object")
	post_id = collection.insert_many(payload)
	print("Object Inserted")
	print(post_id)
except:
	e = sys.exc_info()[0]
	print("error: %s", e)
