""" 
Nombre: persona.py
Objetivo: Ser la superclase en la jerarquía de herencia
Autor: Juan Luis Magaña Paz
Fecha: 20 de septiembre de 2019
"""

class persona(object):
    #Constructor
    def __init__(self, name, ap, sex):
        #definimos los atributos
        self.nombre = name
        self.apellidos = ap
        self.sexo = sex

    #Lista de metodos get: regresa el valor de los atributos de los objetos
    def getName(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getSexo(self):
        return self.sexo
    
    #Lista de métodos set: permiten modificar los atributos de los objetos
    def setNombre(self, name):
        self.nombre = name
    def setApellidos(self, ap):
        self.apellidos = ape
    def setSexo(self, sex):
        self.sexo = sex 
    #Método para imprimir los atributos del objeto
    def personaToString(self):
        return "El nombre es: "+self.nombre + " "+self.apellidos + "con sexo: "+str(self.sexo)
        