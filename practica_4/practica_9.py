#!/usr/bin/env python
# Joshwa
# This code plots the temperature vs time graph online using thingspeak measured by a thermometer.
# The Thermometer value is read by BrickPi mounted on RaspberryPi.
# For more information on BrickPi and Thermometer sensor visit http://www.dexterindustries.com/
# To get started on basics of pushing data to thingspeak visit : www.australianrobotics.com.au/news/how-to-talk-to-thingspeak-with-python-a-memory-cpu-monitor 
# For the working of thermometer code alone visit : https://github.com/DexterInd/BrickPi_Python/blob/master/Sensor%20Examples/DI-dTemp%20test.py
# Connect the Thermometer to the SENSOR PORT_3 of BrickPi
import httplib, urllib
import time
import serial
from BrickPi import *   #import BrickPi.py file to use BrickPi operations
import math
from random import randint

def prueba():
	temp = randint(0,50)
	#params = urllib.urlencode({'field1': temp, 'key':'FCPI0AH7789024OW'})		
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("192.168.10.50:3000")
	arduino = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=3.0)
	try:		
		txt     = arduino.readline()		
		if "Temp" in txt:			
			val     = txt[5:7]		
			conn.request("POST", "/update", {'field1': val, 'key':'QOPT6UV8MICZ7XZA'}, headers)
			response = conn.getresponse()
			print temp
			print response.status, response.reason
			data = response.read()
			conn.close()
		else:
			print "No encontro temperatura"
			print txt
	except:
		print "connection failed"

if __name__ == "__main__":
	while True:
		#thermometer()
		prueba()
		time.sleep(16) 
