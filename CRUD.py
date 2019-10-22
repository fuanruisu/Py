# Nombre: Crud.py
# Objetivo: Crea, Lee, Actualiza y Borra los datos de una lista
# Autor: alumnos de Mecatrónica 
# Fecha: 27 de agosto de 2019

#crear lista vacía 
import os 
lista = []
#Se crea el menú para elegir la operación que quiere realizarse
def menu():
        continuar=True
        while (continuar):
                os.system("cls") #Se limpia lo que hay en la pantalla
                print("1) Create")
                print("2) Read")
                print("3) Update")
                print("4) Delete")
                print("Any key to go out of here!!")
                ho=input("Ingress an option...  ")
                
                if (ho=="1"): create() 
                elif (ho=="2"):
                        os.system("cls")
                        read()
                        #pausa para mantener los datos en pantalla
                        os.system("pause")
                elif (ho=="3"): update()
                elif (ho=="4"): delete()
                else: continuar=False

#Función para crear nuevos datos
def create():
    os.system("cls")
    e=int(input('Ingress the number of entries\n'))
   #Ciclo para ingresar dato por dato
    for i in range(e):
        this=input('Ingress the element\n')
        
        lista.append(this)
        
    

#Función para actualizar datos de la lista
def update():
    os.system("cls")
    x=len(lista)
    read()
    e=int(input('Choose the position you going to change\n'))
    this=input('Ingress the new value\n')
    lista[e-1]=this
    
    
#Función para leer los datos de la lista
def read():
    x=len(lista)
    print('tha list has ',x,'elements')
    for i in lista:
    
        print (i)
#Función para eliminar datos de la lista
def delete():
    os.system("cls")
    x=len(lista)
    read()
    e=int(input('Choose the position you going to delete\n'))
    lista.pop(e-1)
    
    
#Función main 
def main():
    menu()
        

if __name__=="__main__":
    main()
