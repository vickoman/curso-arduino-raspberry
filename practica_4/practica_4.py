#!/usr/bin/env python
from ubidots import ApiClient
import xml.etree.cElementTree as ET
import time
import datetime


api = ApiClient("d66dfcd757f20e235cf72b6040752ae75eb0aa33")
temperature = api.get_variable("59581dff7625423eb19351e9")

tree = ET.parse('temperatura_15_07_2017_15_11_49.xml')
root = tree.getroot() #obtengo la referencia de la raiz
for item in root:  #obtengo los hijos desde la raiz
	try:
		fecha = int(time.mktime(datetime.datetime.strptime(item.attrib["tiempo"], '%d-%m-%Y %H:%M:%S').timetuple()))
    	fecha = int(fecha * 1e3)
    	response = temperature.save_value({"value": int(float(item.text)),
                                       "timestamp": fecha})
    	print("Subiendo...")
    except:
    	pass
    time.sleep(0.5)