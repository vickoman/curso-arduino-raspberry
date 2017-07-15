#!/usr/bin/env python
from ubidots import ApiClient
import xml.etree.cElementTree as ET
import time
import datetime


api = ApiClient("d66dfcd757f20e235cf72b6040752ae75eb0aa33")
temperature = api.get_variable("59581dff7625423eb19351e9")
#humedad = api.get_variable("59581df87625423eb2e5514d")

response_t = temperature.get_values()

if len(response_t):
    root = ET.Element("datos_temperatura")
    for t in response_t:
        temperatura = ET.SubElement(root, "temperatura")
        temperatura.text = str(t['value'])
        temperatura.set('tiempo', datetime.datetime.fromtimestamp(t["timestamp"]/1e3).strftime('%d-%m-%Y %H:%M:%S'))
    tree = ET.ElementTree(root)
    tree.write("temperatura_"+ time.strftime("%d_%m_%Y_%H_%M_%S") +".xml")