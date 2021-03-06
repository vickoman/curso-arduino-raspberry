#!/usr/bin/env python
import serial
import MySQLdb
from random import randint
import time

arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=3.0)
#Mysql connection
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="base_practica")

def save_data_sensor(sensor, value):
	cursor = db.cursor()
	queryinsert = "INSERT INTO data(sensor, valor)VALUES('%s', '%s')" % (sensor, value)
	try:
		cursor.execute(queryinsert)
		db.commit()
		cursor.close()
		print("Se insert el valor")
	except:
		db.rollback()
		print("No se inserto el valor")

while True:	
	txt = arduino.readline()
	time.sleep(10)
	if "Temp" in txt:
		sensor  = 1
		val     = txt[5:7]
		save_data_sensor(sensor, val)

	elif "Hum" in txt:
		sensor  = 2
		val     = txt[4:6]
		save_data_sensor(sensor, val)	


arduino.close()