import serial
import MySQLdb

arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=3.0)
#Mysql connection
#db = MySQLdb.connect(host=arduino, user="root", passwd="root!", db="data")

while True:
	txt = arduino.readline()
	print(txt)

arduino.close()