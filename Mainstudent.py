""" 
Nombre: persona.py
Objetivo: clase que hereda de estudiante
Autor: Juan Luis Magaña Paz
Fecha: 20 de septiembre de 2019
"""

from estudiante import Estudiante

def main():
    ascenciadas = Estudiante("Coacha ","BAstante ",True,"MecaRocks","FIMEBitches","8212")
    #Imprimir el objeto
    print("Objeto modificado b:", ascenciadas.printTLN())

if __name__=="__main__":
    main()