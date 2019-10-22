#importar libreria
import serial
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Prueba_serial"
    )
mycursor = mydb.cursor()
#crear un objeto serial
puerto = serial.Serial("COM3",9600)
while (True):
    try:
        dato = puerto.readline().decode().replace("\n","")
        print("La temperatura es: "+dato) #Limpiamos dato
        sql = "INSERT INTO parametros_agua (temperatura) VALUES ("+str(dato)+")"
        mycursor.execute(sql)
        mydb.commit()

    except:
        print("Ocurrió un Error")
        break
puerto.close