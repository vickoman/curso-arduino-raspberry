import httplib, urllib
import time
import serial
from BrickPi import *   #import BrickPi.py file to use BrickPi operations
import math
from random import randint
arduino = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=3.0)
def prueba():
    global arduino
    while True:
        txt = arduino.readline()
        if "Temp" in txt:
            temp = txt[5:7]
            params = urllib.urlencode({'field1': temp, 'key':'FCPI0AH7789024OW'})     # use your API key generated in the thingspeak channels for the value of 'key'
            # temp is the data you will be seding to the thingspeak channel for plotting the graph. You can add more than one channel and plot more graphs
            headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = httplib.HTTPConnection("192.168.10.49:3000")
            try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print temp
                print response.status, response.reason
                data = response.read()
                conn.close()
            except:
                print "connection failed"
    arduino.close()


#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
        while True:
                #thermometer()
                prueba()
                time.sleep(16) 
