""" 
Nombre: Cilindro.py
Objetivo: Construye objeto tipo punto en el cilindro
Autor: Juan Luis Magaña Paz
Fecha: 20 de septiembre de 2019
"""
from Circunferencia import Circunferencia
import math 
class Cilindro(Circunferencia):
    #Método constructor
    def __init__(self,valorX,valorY, vRadio,vAlt):
        self.x = valorY
        self.y = valorX
        self.radio = vRadio
        self.altura = vAlt
    #Método get 
    def getAltura(self):
        return self.altura
    #Método set
    def setAltura(self, vAlt):
        self.altura = vAlt
    #Método para calcular el volumen del Cilindro
    def getVolumen(self):
        self.getArea()*self.getAltura()

    #Método para imprimir el objeto cilindro
    def printCilindro(self):
        return "La circunferencia con centro en: "+str(self.x)+","+str(self.y)+"y radio igual a: "+str(self.radio)+"y el area es: "+str(self.getArea())+" y altura igual a: "+str(self.Altura)+" y el volumen del cilindro es: "+str(self.getVolumen())