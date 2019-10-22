#Nombre: Nómina
#Objetivo: Permite el cálculo de sueldo por trabajador y el 
#sueldo global generado por la nómina
#Autor: Juan Luis Magaña Paz
#Fecha:29 de Agosto de 2019

#Variables globales
import os
name = ""
dt = 0
st = 0
he = 0
she = 0
nt = 0
sg = 0
nombre = []
wdays = []
sdiario = []
et=[]
stotal=[]
def menu():
    global sg
    global nt
    print("-- Aplicacion de nómina --")
    ciclo="S"
    while ciclo == "S" or ciclo == "s":
        os.system("cls")
        name = input("Nombre del trabajador:\n")
        dt=int(input("Días trabajados (1...15)\n"))
        sd=float(input("Sueldo diario:\n"))
        he= int(input("Horas extras laboradas:\n"))
        nombre.append(name)
        wdays.append(dt)
        sdiario.append(sd)
        et.append(he)

        #Calculamos el sueldo del trabajador
        st = (dt * sd)+he*100
        stotal.append(st)
        print("El sueldo del trabajador es:\n", st)
        #Acumular sueldo
        sg=sg+st
        #Cuenta de los trabajadores
        nt=nt+1
        #Preguntamos si quiere ingresar sueldo de otro trabajador
        ciclo = input("¿Desea agregar otro empleado? (S/N)")
        os.system("cls")
        print("Cálculo total de la nómina: ")
        print("Número de trabajadores: ", nt)
        print("Monto de la nómina", sg)
    
        for i in range(nt):
            print("Nombre: ",nombre[i]," Dias lab: ",wdays[i]," S. diario: ",sdiario[i]," Hrs. ext: ",et[i]," Sueldo: ",stotal[i],"\n")
            










def main():
    menu()
    
    
if __name__=="__main__":
        main()

    