"""
Nombre: conectar.py
Objetivo : Abre una conexión a la base de datos mysql
Autor: juan Luis Magaña Paz
"""

#Importamos la librería mysql
import pymysql 
#Abre conexión con la base de datos crud
db= pymysql.connect("localhost","root","","crudpython")

#prepare a cursor object using cursor() method
cursor = db.cursor()

sqlcad="INSERT INTO empleados(clave,nombre,sueldo) VALUES (3,'Achencho eat dongs',-500)"
#Ejecuta el SQL query usando el metodo execute().
cursor.execute(sqlcad)
#commit your changes in the database
db.commit()
print("Operación realizada...")

#desconecta del servidor
db.close()