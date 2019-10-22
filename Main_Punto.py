""" 
Nombre: Main_Punto.py
Objetivo: Construye objeto tipo punto en el plano cartesiano
Autor: Juan Luis Magaña Paz
Fecha: 20 de septiembre de 2019
"""
from Punto import Punto

def main():
    a = Punto(2,3)
    b = Punto(-3,6)
    #Invocar método de impresión
    print("Objeto a: ", a.printPunto())
    print("Objeto b: ", b.printPunto())
    #Invocar método set del objeto b 
    b.setX(3)
    b.setY(6)
    print("Objeto modificado b:", b.printPunto())


if __name__=="__main__":
    main()