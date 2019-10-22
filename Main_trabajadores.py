"""
Nombre: Trabajador.py
Objetivo: Construye objetis tipo Trabajador
Autor: Alumnos de Mecatrónica
Fecha: 17 de septiembre de 2019
"""
from Trabajador import Trabajador
#Crear objetos
def main():
    chuyv = Trabajador(1,"Jesús Alberto Verduzco",23.12)
    canoEatD=Trabajador(4,"Cano CO. me D",1000)
    #Invocar métodos get
    chuyv.printObjeto()
    #Utilizar métodos set
    chuyv.setClave(2)
    chuyv.setNombre("Chuy Verduras")
    chuyv.setSueldo(2345.12)


    
    #Imprimir modificaciones del objeto
    #Invocar métodso get
    chuyv.printObjeto()
    canoEatD.printObjeto()
    

if __name__=="__main__":
    main()