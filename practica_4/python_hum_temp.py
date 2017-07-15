import serial

arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=3.0)

while True:
	txt = arduino.readline()
	print(txt)