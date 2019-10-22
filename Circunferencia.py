""" 
Nombre: Circunferencia.py
Objetivo: Construye objeto tipo punto en la circunferencia
Autor: Juan Luis Magaña Paz
Fecha: 20 de septiembre de 2019
"""
from Punto import Punto
import math
class Circunferencia(Punto):
    #Método constructor
    def __init__(self,valorX,valorY, vRadio):
        self.x = valorY
        self.y = valorX
        self.radio = vRadio
    #Método get
    def getRadio(self):
        return self.radio
    #Método set 
    def setRadio(self,vRadio):
        self.radio = vRadio
    #Método para calcular el área de la circunferencia
    def getArea(self):
        return math.pi * math.pow(self.radio,2)

    #Método para imprimir los atributos del objeto circunferencia
    def printCirc(self):
        return "La circunferencia con centro en: "+str(self.x)+","+str(self.y)+"y radio igual a: "+str(self.radio)+"y el area es: "+str(self.getArea())
