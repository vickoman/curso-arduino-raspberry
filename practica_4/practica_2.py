#!/usr/bin/env python
from ubidots import ApiClient
import time
from random import randint

api = ApiClient("kKWPshWijlTpR1BzDbVK9YALXi48Uf")
temperature = api.get_variable("59581dff7625423eb19351e9")
humedad = api.get_variable("59581df87625423eb2e5514d")

while(1):
	try:
		response = temperature.save_value({"value": randint(0,10)})
		response = humedad.save_value({"value": randint(0,10)})
	except:
		pass
	time.sleep(5)