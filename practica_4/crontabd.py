import time
while True:
	archivo = open("/var/log/piscriptlog.log", 'a')
	fecha = time.strftime("%Y-%m-%d %H:%M:%S")
	archivo.write(fecha)
	archivo.write("\n")
	archivo.close()
	time.sleep(5)
