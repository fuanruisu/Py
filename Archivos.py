#Nombre: archivos.py
#Objetivo: Muestra la funcionalidad de los archivos
#Autor: Juan Luis Magaña Paz
#Fecha: 6 de septiembre de 2019
import os
os.system("cls")
#Crear o abrir archivos 
archivo = open("file.txt","w")
#Insertar datos en el archivo
archivo.write("Hola motherfuckings niggas")
#Cerrar el archivo
archivo.close()

#Imprime todo el archivo
archivo = open("file.txt","r")
print(archivo.read())
archivo.close() 

#Abrimos archivo con parametros de modificacion
archivo = open("file.txt","a")
archivo.write("\nHello n")
# cerrar archivo
archivo.close

#Imprime linea por linea 
archivo = open("file.txt","r")
for linea in archivo.readlines():
    print(linea)
archivo.close() 

