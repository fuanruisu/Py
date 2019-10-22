# Nombre: listas.py
# Objetivo: crear  una listas
import os
lista=["Hola", "h0l4","como","estas","?"]
def crear():
    lista.append(input("==> Ingrese: "))
def leer():
        print("***Lista***")
        j=0
        for i in lista:
                j=j+1
                print (j,") ",i)



def actualizar():
        os.system("cls")
        print("==ACTUALIZAR==")
        leer()
        posicion=int(input("==> Cual vas a modificar?: "))
        entrada=input("==> Ingresa el dato nuevo: ")
        lista[posicion-1]=entrada

def borrar():
        os.system("cls")
        print("==Borrar==")
        leer()
        posicion=int(input("==> Cual vas a borrar?: "))
        lista.pop(posicion-1)
        print("Elemento borrado...")
        os.system("pause")

def menu():
        continuar=True
        while (continuar):
                os.system("cls")
                print("1) Crear")
                print("2) Leer")
                print("3) Actualizar")
                print("4) Borrar")
                print("5) Finalizar")
                entrada=input("==> ")
                
                if (entrada=="1"): crear() 
                if (entrada=="2"):
                        os.system("cls")
                        leer()
                        os.system("pause")
                if (entrada=="3"): actualizar()
                if (entrada=="4"): borrar()
                if (entrada=="5"): continuar=False
                

def main():
        #print(lista[1])
        menu()
        os.system("cls")
        

if __name__=="__main__":
    main()