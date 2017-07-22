from ubidots import ApiClient
import MySQLdb
import httplib
import datetime
import time
import logging


logger = logging.getLogger('enviarUbidots')
handler = logging.FileHandler('/var/log/enviarUbidots.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.info('Iniciando script enviarUbidots')


#Create an "API" object
api = ApiClient(token='kKWPshWijlTpR1BzDbVK9YALXi48Uf')
con = MySQLdb.connect(host="localhost",user="root",passwd="root",db="base_practica")
try:
    variable_tmp = "59581dff7625423eb19351e9"
    variable_hum = "59581df87625423eb2e5514d"
    while 1:
        time.sleep(20)
        cursor = con.cursor()
        cursor.execute("SELECT id,sensor,valor,fecha_registro FROM data WHERE enviado=0 ORDER BY fecha_registro ASC;") 
        reg     = cursor.fetchone()
        if len(reg) != 0:
            try:
                id_sensor   = reg[0]
                sensor      = reg[1]
                valor       = reg[2]
                fecha_db       = reg[3]
                logger.info("sensor=%s valor=%s",sensor,valor)
                if sensor==1:               
                    variable = api.get_variable(variable_tmp)
                else:
                    variable = api.get_variable(variable_hum)   
                resultado = variable.save_value({'value': valor, 'timestamp': datetime.time(fecha_db).strftome("%s")})   
                logger.info(resultado)
                sql = """UPDATE data SET enviado = 1 WHERE id = %s"""
                cursor.execute(sql,(id_sensor))
                con.commit()                
                logger.info('Guardado exitoso..')
            except Exception,e:
                logger.error('Error al guardar valor en ubidots')
                cursor.close()  
        else:
            logger.error('error al consultar')
except Exception,e:
    logger.error(str(e))
    logger.error('Error en la conexion ubidots...')
        