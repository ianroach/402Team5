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

greaterThan = float(input("Your number will be greater than: "))
lessThan = float(input("Your number will be less than: "))
digits = int(input("Your number will be how many decimal digits: "))


@app.route('/run_post')
def run_post():

       rounded_number = round(random.uniform(greaterThan, lessThan), digits)

       url = 'http://iansraspberrypi:5000/'
       data = {'temperature': rounded_number, 'team id': 5, 'pi id': 2, 
		'currentTime': now.strftime("%H:%M"), 'currentDate': now.strftime("%m-%d-%Y"), 'Measurement': 'farenheit'}
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
