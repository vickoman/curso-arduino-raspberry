import time
while True:
	archivo = open("log.txt", 'a')
	fecha = time.strftime("%Y-%m-%d %H:%M%S")
	archivo.write(fecha)
	archivo.write("\n")
	archivo.close()
	time.sleep(5)
