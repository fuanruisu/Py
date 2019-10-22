#Nombre: inventario.py
#Objetivo: Crea un archivo csv con el inventario ingresado
#Autor: Juan Luis Magaña Paz
#Fecha: 06 de septiembre de 2019
import os
concepto=[]
cant=[]
model=[]
caja=[]
#creación del diccionario
param = {"Concepto":concepto, "Cantidad":cant,"Modelo": model,"Caja":caja}
    
#Se crea un archivo csv en el cual se colocan por columna las keys del diccionario y se rellenan
# con sus respectivos valores
def csv():
    # Se obtienen las keys del diccionario
    keys=param.keys()
    #Se abre un archivo de tipo csv de nombre datos_Metereologicos
    archivo = open("Inventario.csv","w")
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
    op=len(model)
    for j in range(op):
        #El segundo for es para acceder a las distintas keys del diccionario
        for i in keys:
            #Se obtienen los valores 
            m=str(param[i][j])
            #Se escriben en el archivo csv el ; delimita por columnas cada valor
            archivo.write(m+";")
        #Se realiza un salto de linea para continuar con la siguiente posición de las keys
        archivo.write("\n")
    #Cerramos el archivo
    archivo.close()
        
def main():  
    state=True
    print("Bienvenido ingrese los datos")
    while state==True:
        
        h=(input("Concepto:\n"))
        concepto.append(h)
        h1=(input("Cantidad:\n"))
        cant.append(h1)
        h2=(input("Modelo:\n"))
        model.append(h2)
        h3=(input("Caja:\n"))
        caja.append(h3)
        change=(input("¿Desea ingresar otro dato?(s/n)\n"))
        os.system("cls")
        if (change=='N' or change=='n'):
            state=False
    

    csv()

 
if __name__=="__main__":
    main()