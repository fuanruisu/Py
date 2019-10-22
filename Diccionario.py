#Nombre: Diccionario.py
#Objetivo: Muestra la funcionalidad de los diccionarios en python
#Autor: Juan Luis Magaña Paz
#Fecha: 30 de agosto de 2019
import math
import random

def regresarRandom():
    return random.randrange(1,100,1)

def main():
    estudiantes = {} #dicccionario vacío
    prof = {"nombre":"Armando Gaytán"}
    param = {"temperatura": 27, "humedad":"87%","presión": "160 mmhg","lluvia":False}
    #Insertar un ítem en un diccionario
    param["velocidadViento"]="35 km/hr"
    #Consultar un ítem del diccionario
    print(param["presión"])
    #modificar el valor de un ítem de un diccionario
    param["humedad"]="92%"
    #Imprimir todos los ítems del diccionarios

    for i in param:
        print(i)
    print("El número aleatorio es: ",regresarRandom())


if __name__=="__main__":
        main()