"""
Nombre: Trabajador.py
Objetivo: Construye objetos tipo Trabajador
Autor: Juan Luis Magaña Paz 
Fecha: 17 de septiembre de 2019
"""

class Trabajador():
    #Constructor: instancia la clase para construir objetos
    def __init__(self,code, name, sal):
        print("--Creando nuevo objeto--")
        self.clave = code
        self.nombre = name
        self.sueldo = sal
    # Lista de métodos get: regresan valor de atributos
    def getClave(self):
        return self.clave
    def getNombre(self):
        return self.nombre
    def getSueldo(self):
        return self.sueldo
    #Lista de métodos set: modificamos atributos del objeto
    def setClave(self, code):
        self.clave = code
    def setNombre(self,name):
        self.nombre = name
    def setSueldo(self, sal):
        self.sueldo = sal
    def printObjeto(self):
        #Invocar métodos get
        print("Clave:",self.getClave(),"\n",
        "Nombre:",self.getNombre(),"\n",
        self.getSueldo())

    


