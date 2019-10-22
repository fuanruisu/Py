#Nombre: quiz2.py
#Objetivo: Crea un archivo csv con datos creados aleatoriamente
#Autor: Juan Luis Magaña Paz
#Fecha: 06 de septiembre de 2019
import math
import random
import time
fecha=[]
hr=[]
temp=[]
hum=[]
P=[]
Ws=[]
rumbo=[]
#creación del diccionario
param = {"Fecha":fecha, "Hora":hr,"Temperatura": temp,"Humedad": hum,"Presion": P,"Wind speed": Ws,"Rumbo": rumbo}
    
#genera rumbos aleatorios (string aleatorio)
def rwind():
    lista = ["N", "NNE", "NEE", "E", "SEE", "SSE","S","SSW","SWW","W","WNW","NNW"]
    return random.choice(lista)

#genera un numero aleatorio de 1 a 100
def rnumber():
    return random.randrange(1,100,1)

    
#Se crea un archivo csv en el cual se colocan por columna las keys del diccionario y se rellenan
# con sus respectivos valores
def csv():
    # Se obtienen las keys del diccionario
    keys=param.keys()
    #Se abre un archivo de tipo csv de nombre datos_Metereologicos
    archivo = open("datos_Metereologicos.csv","w")
    archivo.write("Made By:;Juan;Luis;Magaña;Paz")
    archivo.write("\n")
    #Se guardan en el archivo las keys por columnas
    for i in keys:
        # El ; es para colocar en una columna distinta las keys del diccionario
        archivo.write(i+";")

    #Se ejecuta un salto de linea al terminar de escribir las keys
    archivo.write("\n")
    
    #Se llenan los valores en el archivo
    #El primer for es para acceder a las posiciones de las keys
    op=len(P)
    for j in range(op):
        #El segundo for es para acceder a las distintas keys del diccionario
        for i in keys:
            #Se obtienen los valores 
            h=str(param[i][j])
            #Se escriben en el archivo csv el ; delimita por columnas cada valor
            archivo.write(h+";")
        #Se realiza un salto de linea para continuar con la siguiente posición de las keys
        archivo.write("\n")
    #Cerramos el archivo
    archivo.close()
        
def main():
   
    #las claves son las variables climaticas y los valores listas
    
    #Variables para acumular los valores de las variables climáticas
    promtemp=0
    promhum=0
    promP=0
    promWs=0

    #for para hacer el llenado de las listas
    for i in range(500):
            #Asignación de valores aleatorios
            temp1=rnumber()
            hum1=rnumber()
            P1=rnumber()
            Ws1=rnumber()
            #acumulación de los valores de variables climáticas
            promtemp=promtemp+temp1
            promhum=promhum+hum1
            promWs=promWs+Ws1
            promP=promP+P1
            #Llenado de la lista fecha
            fecha.append(time.strftime("%x"))
            #Llenado de la lista hora
            hr.append(time.strftime("%X"))
            #Llenado de las variables climáticas
            temp.append(temp1)
            hum.append(hum1)
            P.append(P1)
            Ws.append(Ws1)
            #Llenado del rumbo del viento con la funcion de string aleatorio
            rumbo.append(rwind())
   
    csv()

 
if __name__=="__main__":
        main()