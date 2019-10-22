lista=["m","G","a","b","c","d","e","f"]
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
archivo = open("file.csv","w")
#Insertar datos en el archivo
for i in diccionario:
        archivo.write(i+";")
keys=diccionario.keys()
for i in keys:
        print(diccionario[i])
print(keys)
print(diccionario["cursos"][0])
#Cerrar el archivo
archivo.close()