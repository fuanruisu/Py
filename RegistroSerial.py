# Nombre: receivefromArduino.py
# Objetivo: lee los datos enviados por Arduino y guardarlos en un archivo
# Autor: alumnos de SE de 2018
# Fecha: 13 septiembre de 2018


# importar libreria
import serial
import datetime

#-----------------------------------------
# Metodo para escribir datos en un archivo
#------------------------------------------
def escribeDatoInFile(data):
    f = open('datos.txt', 'a')
    f.write(str(data))

# Crear un objeto serial
puerto = serial.Serial("COM6", 9600)

#variable para saber que son los encabezados
bandera=0

while (True):
    
    if (bandera==0):
        bandera=1
        escribeDatoInFile("temperatura,timestamp"+"\n")
    else:    
        t = datetime.datetime.now()
        fecha = str(t.year)+'-'+str(t.month)+'-'+str(t.day)
        hora = str(t.hour)+':'+str(t.minute)+':'+str(t.second)


        dato = puerto.readline().decode().replace("\n", "")  # Lee buffer del puerto serie
        print("La temperatura del agua es: "+dato)
        # Invocamos funcion
        escribeDatoInFile(str(dato+","+fecha+" "+hora+"\n"))

puerto.close
