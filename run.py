# Project: Lab 6 Client and Server Using Eve on Linux, CURL, CRUD with MongoDB
# Purpose Details: To learn how to use the Eve RESTful server to communicate 
# Course: IST 411
# Author: Joshua Gonzales
# Date Developed: 10/1/2024
# Last Date Changed: 10/1/2024
# Rev: 1


from eve import Eve

eveApp = Eve(settings = 'people.py')

if __name__ == '__main__':
	eveApp.run(port=5000)


