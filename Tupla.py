#Nombre: Tupla.py
#Objetivo: Muestra la funcionalidad de las tuplas en Python
#Autor: Juan Luis Magaña Paz
#Fecha: 03 de septiembre de 2019

# Una tupla es una estructura de datos inmutable

# tupla vacía
t1=() 
# tupla con elementos
t2=("Que traes Perro",12.33,3,-5,False,"234.56")
# Preguntar número de elementos de la tupla 
print ("Número de elementos de la tupla: ", len(t1),",",len(t2))
# Imprimir elementos de la tupla
print(t2[0])
print(t2[:3])
print(t2)

# Quiz. Escriba un script en python que permita almacenar como 
# ítem de la tupla los elementos de una lista. Defina una lista de 
# al menos 5 elementos, insertar en la tupla e impriman la tupla

lista=["M", "A","G","A","Ñ"]
t3=(lista)
print(t3)
lista.pop(3)
print(t3)
# Quiz 2. Ingrese 1000 elementos, ordenarlos método sort, imprimirlos

