"""
Nombre: buscar.py
Objetivo : Busca registros en una base de datos
Autor: juan Luis Magaña Paz
"""

#Importamos la librería mysql
import pymysql 
#Abre conexión con la base de datos crud
db= pymysql.connect("localhost","root","","crudpython")

#prepare a cursor object using cursor() method
cursor = db.cursor()

sqlcad="SELECT * FROM empleados;"
#Ejecuta el SQL query usando el metodo execute().
cursor.execute(sqlcad)
#commit your changes in the database
db.commit()
resultado = cursor.fetchall()
for row in resultado:
    clave = row[0]
    nombre = row[1]
    sueldo = row[2]
    #Now print fetched result
    print("id={0},nombre={1},sueldo={2}".format(clave,nombre,sueldo))

print("Operación realizada...")

#desconecta del servidor
db.close()