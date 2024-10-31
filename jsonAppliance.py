#Project: W2 Solo Lab Python3 and JSON Appliance Object
#Purpose Details: Read and Write to JSON Files using Python3
#Course: IST411
#Author: Joshua Gonzales
#Date Developed: 9/5/2024
#Last Date Changed: 9/5/2024
#Rev: 2

import json

class Microwave:
	def __init__(self, make, model, year, color, wattage, serialNumber, spinPerMinute):
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.wattage = wattage
		self.serialNumber = serialNumber
		self.spinPerMinute = spinPerMinute

joshsMicrowave = Microwave('Samsung','Bespoke', 2022, 'Black', 1000, 'BOTRM202277362',7)

with open('jsonAppliance.json','w') as outFile:
	jsonObjAppliance = outFile.write(json.dumps(joshsMicrowave.__dict__))
print (joshsMicrowave.__dict__)
