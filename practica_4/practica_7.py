import serial
import MySQLdb
import time
import logging

logger = logging.getLogger('guardarBD')
handler = logging.FileHandler('/var/log/guardarBD.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.info('Iniciando script guardarBD')

while True:
    try:
        con = MySQLdb.connect(host="localhost",user="root",passwd="root",db="base_practica")
        arduino = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=3.0)
        txt = ''
        time.sleep(10)
        while True:
            try:
                time.sleep(10)
                txt     = arduino.readline()
                time.sleep(5)
                cursor  = con.cursor()
                sql     = """INSERT INTO data(sensor,valor) VALUES(%s,%s)"""
                val     = ""
                sensor  = 0
                if "Temp" in txt:
                        sensor  = 1
                        val     = txt[5:7]
                        logger.info('Ingresando tmp %s',val)
                elif "Hum" in txt:
                        sensor  = 2
                        val     = txt[4:6]      
                        logger.info('Ingresando hum %s',txt[4:6])   
                
                if sensor==1 or sensor==2:
                    cursor.execute(sql,(sensor,val))
                    con.commit()
                cursor.close()              
            except Exception, e:
                logger.error(str(e))
                con.rollback()          
        arduino.close()
        con.close()
    except Exception, e:
        logger.error(str(e))
        time.sleep(10)  