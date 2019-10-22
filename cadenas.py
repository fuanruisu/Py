#Nombre: cadenas.py
#Objetivo: Muestra la funcionalidad de las cadenas de carácteres
#Autor: Juan Luis Magaña Paz
#Fecha: 03 de septiembre de 2019

# definir cadena
cad = "Hola mundo"
cad1= " loco"
car="slkklalsalaskaslñkaslk"
print(cad)
print(car)

# Concatenación de cadenas
print(cad +   cad1)
# Multiplicación de cadenas
cad3 = cad + cad1*3
print(cad3)
#Obtener el número de elemento de una cadena (longitud)
print(len(cad3))
car=""
print(len(car))
#Convertir a mayúsculas
min="kladmlAsdklasd"
may=min.upper()
print(may)
min=may.lower()
print(min)
# Encontrar una subcadena en una cadena
cad3="Hola mundo loco loco loco loco"
subcadena=cad3.find("loco")
print(subcadena)
#Espacio en blanco
print(cad3.find(" "))
#Un carácter que no esta en la cadena
print((cad3.find("X")))
cs='hola\"cerdo"'
print(cs.find('\"cerdo"'))
# Reemplazar
briand = "Briand alfredo"
pos=(briand.find("a"))
print(pos)
#sustitución
x=briand.replace("a","A")
print(x)
#Cortar cadenas 
print(cad3[0:10])