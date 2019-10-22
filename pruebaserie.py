#Nombre: receivefromArduino.py
#Objetivo: lee los datos enviados por arduino y los guarda en un archivo
#importar libreria 
import serial 
import datetime
#Metodo para escribir datos en un archivo
def escribeDatoInFile(data):
	f = open('datos.txt', 'a')
	f.write(str(data))

	#crear un objeto serial
puerto = serial.Serial("COM6",9600)

while (True):
		if (bandera==9):
			bandera=1
			escribeDatoInFile("temperatura")
		t = datetime.datetime.now()
		fecha = str(t.year)+'-'+str(t.month)+'-'+str(t.day)
		hora = str(t.hour)+':'+str(t.minute)+':'+str(t.second) 


		dato = puerto.readline().decode().replace("\n","") #Lee buffer del puerto serie
		cadena = str(dato)+","+fecha+" "+hora
		print("La temperatura del agua es: "+dato)#limpiamos el dato
		print("el tiempo es "+fecha+" "+hora)
		#Invocamos función 
		escribeDatoInFile(str(dato+","+fecha+" "+hora+"\n"))

	

puerto.close
