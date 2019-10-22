#Nombre: quiz.py
#Objetivo: Realizar el tabulado de las variables climáticas generadas aleatoriamente
#Autor: Juan Luis Magaña Paz
#Fecha: 30 de agosto de 2019
from tabulate import tabulate
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
#genera rumbos aleatorios (string aleatorio)
def rwind():
    lista = ["N", "NNE", "NEE", "E", "SEE", "SSE","S","SSW","SWW","W","WNW","NNW"]
    return random.choice(lista)
#genera un numero aleatorio de 1 a 100
def rnumber():
    return random.randrange(1,100,1)


def main():
    #creación del diccionario
    param = {"Fecha":fecha, "Hora":hr,"Temperatura": temp,"Humedad": hum,"Presión": P,"Wind speed": Ws,"Rumbo": rumbo} #dicccionario vacío
    #las claves son las variables climaticas y los valores listas
    
    #Variables para acumular los valores de las variables climáticas
    promtemp=0
    promhum=0
    promP=0
    promWs=0

    #for para hacer el llenado de las listas
    for i in range(100):
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
                                       
              

        


   #Obtención de los promedios
    promtemp=promtemp/100
    promP=promP/100
    promWs=promWs/100
    promhum=promhum/100
    #Llenado de la ultima fila con los promedios obtenidos
    fecha.append(time.strftime("%x"))
    hr.append(time.strftime("%X"))
    temp.append(promtemp)
    hum.append(promhum)
    P.append(promP)
    Ws.append(promWs)
    rumbo.append("Promedio")
    #Tabulación del diccionario
    print(tabulate(param, headers='keys', tablefmt='fancy_grid'))

    
    


if __name__=="__main__":
        main()