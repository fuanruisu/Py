import pymysql 

# Abrir conexión a la base de datos 
db = pymysql.connect("localhost", "root", "","semaforo",)
# Creamos un objeto tipo de cursor
cursor = db.cursor()

#Enviar comandos sql a la base de datos 
cursor.execute("insert into estrategias(id,horario,tr,tv,ta) values ("sem3", "7-10",32,3,45);")

#Cerramos conexion
db.close