"""
Nombre: conectar_D.py
Objetivo : Abre una conexión a la base de datos mysql
Autor: juan Luis Magaña Paz
"""

#Importamos la librería mysql
import pymysql 
#Abre conexión con la base de datos crud
db= pymysql.connect("localhost","root","","id11100102_meca")

#prepare a cursor object using cursor() method
cursor = db.cursor()

sqlcad="INSERT INTO empleados(clave,descripcion,precio) VALUES (3,'Achencho eat dongs',-500)"
#Ejecuta el SQL query usando el metodo execute().
cursor.execute(sqlcad)
#commit your changes in the database
db.commit()
print("Operación realizada...")

#desconecta del servidor
db.close()