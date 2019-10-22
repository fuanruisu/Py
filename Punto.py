""" 
Nombre: Punto.py
Objetivo: Construye objeto tipo punto en el plano cartesiano
Autor: Juan Luis Magaña Paz
Fecha: 20 de septiembre de 2019
"""
class Punto(object):
    #Método constructor
    def __init__(self, valorX, valorY):
        #definimos atributos de la clase
        self.x = valorX
        self.y = valorY

        #Lista de métodos get
    def getX(self):
            return self.x

    def getY(self):
            return self.getY
        #Lista de métodos set 
    def setX(self, valorX):
            self.x = valorX
    def setY(self,valorY):
            self.y = valorY
    def printPunto(self):
            return "Coordenadas del punto: "+str(self.x)+", "+str(self.y)
