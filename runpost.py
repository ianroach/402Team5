import json
import smtplib
import requests
import flask

import RPi.GPIO as GPIO
import datetime, time, socket, random

from flask import Flask
app = Flask(__name__)
now = datetime.datetime.now()

from time import sleep

piId = int(input("Enter your pi ID: "))
if piId == 2:
	print("You will see random temperature between 40 and 70.")
	greaterThan = 40
	lessThan = 70
	digits = 2
	#greaterThan = float(input("Your number will be greater than: "))
	#lessThan = float(input("Your number will be less than: "))
	#digits = int(input("Your number will be how many decimal digits: "))
elif piId == 5:
	print("You will see random percentage between 0 and 100")
	greaterThan = 0
	lessThan = 100
	digits = 0
elif piId == 3:
	print("You will see random boolean value")
	greaterThan = 0
	lessThan = 100
	digits = 0
elif piId == 4:
	print("You will see random boolean value")
	greaterThan = 0
	lessThan = 100
	digits = 0




@app.route('/run_post')
def run_post():

	rounded_number = round(random.uniform(greaterThan, lessThan), digits)
	random_bool = random.choice([True, False])

	url = 'http://iansraspberrypi:5000/'
	
	if piId == 2:
		data = {'temperature': rounded_number, 'team id': 5, 'pi id': piId, 
			'currentTime': now.strftime("%H:%M"), 'currentDate': now.strftime("%m-%d-%Y"), 'Measurement': 'farenheit'}
	elif piId == 5:
		data = {'humidity': rounded_number, 'team id': 5, 'pi id': piId, 
			'currentTime': now.strftime("%H:%M"), 'currentDate': now.strftime("%m-%d-%Y"), 'Measurement': 'percentage'}
	elif piId == 3:
		data = {'sound': random_bool, 'team id': 5, 'pi id': piId, 
			'currentTime': now.strftime("%H:%M"), 'currentDate': now.strftime("%m-%d-%Y"), 'Measurement': 'yes or no'}
	elif piId == 4:
		data = {'light': random_bool, 'team id': 5, 'pi id': piId, 
			'currentTime': now.strftime("%H:%M"), 'currentDate': now.strftime("%m-%d-%Y"), 'Measurement': 'yes or no'}
	headers = {'Content-Type' : 'application/json'}

	r = requests.post(url, data=json.dumps(data), headers=headers)

	#return json.dumps(r.json(), indent=4)
	return r.text
if __name__ == "__main__":

	#GPIO.setmode(GPIO.BCM)

	#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#print('Press button to display data')       
	#while True:
		#input_state = GPIO.input(18)
		#if input_state == False:
			#run_post()
			#time.sleep(0.2)

	print("Sending data..CTRL-C to exit")
	while True:
		run_post()
		time.sleep(3)
