# Nombre: listas.py
# Objetivo: muestra la funciòn de las listas en python
# Autor: alumnos de Mecatrònica 
# Fecha: 27 de agosto de 2019

#crear lista vacía 
lista = []


# agregamos elementos a la lista
lista.append("hola")
lista.append(False)
lista.append(23.13)
lista.append('c')
lista.append(23)
lista.append(-12)

print(lista[1])
# Imprimir los elementos de una lista 
print(lista)
#Imprimir
for i in lista:
    print(i)
n=len(lista)
for i in range(n):
   lista.pop(0)
# Imprimir un item de la lista por medio de su indice
#print("Item en: ", lista[0])