# coding: utf-8
import random
from sense_hat import SenseHat

#sense = SenseHat()
#sense.clear()

class BME280SensorSimulator:

    def __init__(self):
        #pass

	self.sense = SenseHat()

    def read_temperature(self):
        #Microsoft example
	#return random.uniform(20, 30)

	self.sense.clear()
	temperature = self.sense.get_temperature()
	farenheit = ((temperature * 9) / 5) + 32
	return farenheit

    def read_humidity(self):
        #Microsoft example
	#return random.uniform(60, 80)

	self.sense.clear()
	humidity = self.sense.get_humidity()
	return humidity