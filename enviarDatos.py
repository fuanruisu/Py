# Nombre: enviarDatos.py
# Objetivo: envía datos por el puerto serial
# Autor: Alumnos de mecatrónica
# Fecha: 12 de septiembre de 2019

#importar libreria serial
import serial
import time
s=True
#crear objeto serial
puerto=serial.Serial("COM6", 9600)

#funcion encender led
def encenderled():
    puerto.write('1'.encode())
    time.sleep(2)

#funcion apagar led:
def apagarLed():
    puerto.write('0'.encode())
    time.sleep(2)
def main():
    
    while(True):
        encenderled()
        apagarLed()

if __name__=="__main__":
    main()