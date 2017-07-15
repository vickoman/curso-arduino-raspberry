#!/usr/bin/env python
from ubidots import ApiClient
import MySQLdb
import httplib
import time
#Create an "API" object
api = ApiClient(token='kKWPshWijlTpR1BzDbVK9YALXi48Uf')
con = MySQLdb.connect(host="localhost",user="root",passwd="root",db="base_practica")
try:
    variable_tmp = "59581dff7625423eb19351e9"
    variable_hum = "59581df87625423eb2e5514d"
    while 1:
        time.sleep(20)
        cursor = con.cursor()
        cursor.execute("SELECT id,sensor,valor FROM data WHERE enviado=0 ORDER BY fecha_registro ASC;") 
        reg     = cursor.fetchall()
        if len(reg) != 0:
            try:
                id_sensor   = reg[0]
                sensor      = reg[1]
                valor       = reg[2]
                print("sensor=%s valor=%s"%(sensor,valor))
                print("id_sensor=%s sen=%s"%(id_sensor[0],sensor[0]))
                if sensor==1:               
                    variable = api.get_variable(variable_tmp)
                else:
                    variable = api.get_variable(variable_hum)   
                resultado = variable.save_value({'value': valor[0]})
                print resultado         
                sql = """UPDATE data SET enviado = 1 WHERE id = %s"""
                cursor.execute(sql,(id_sensor[0]))
                con.commit()                
                print "Guardado exitoso.."
            except Exception,e:
            	print("Error:%s"%str(e));
                print "Error al guardar valor en ubidots"
            cursor.close()  
        else:
            print "error consulta\n"
except Exception,e:
    print("Error:%s"%str(e));   
    print "error en la conexion ubidots...\n"