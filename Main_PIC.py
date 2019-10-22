"""
Nombre: Main_PIC.py
Objetivo: Construye objetos tipo PIC
Autor: Juan Luis Magaña Paz
Fecha: 17 de septiembre de 2019
"""

from PIC import PIC
#Crear objetos
def main():
    PIC16f877A = PIC(1,"Microchip","16f877A", 20, 1901, 131,1123, 1231)
    PIC16f88A=PIC(1,"Microchip","16f88A", 10, 19, 11,23, 231)
    
    #Invocar métodos get
    #PIC16f877A.printAtributos()

    
    PIC16f877A.printAtributos()
    PIC16f88A.printAtributos()

   
    

if __name__=="__main__":
    main()