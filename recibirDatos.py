# Nombre: recibirDatos.py
# Objetivo: recibe datos por el puerto serial
# Autor: Alumnos de mecatrónica
# Fecha: 12 de septiembre de 2019

import serial 
import time

#Declaramos un objeto serial
puerto = serial.Serial("COM6",9600)
#--------------------------------------------
#función para escribir los datos en archivo
#--------------------------------------------

def escribeArchivo(dato):
    #abrimos archivo
    file=open("datos.txt","a")
    file.write(str(dato))



#Leemos datos
while(True):
    dato = puerto.readline() #Leer buffer del puerto
    print(dato.decode().replace("\n",""))
    escribeArchivo(dato.decode().replace("\n",""))

#Cerramos puerto
puerto.close()