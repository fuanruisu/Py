""" 
Nombre: persona.py
Objetivo: clase que hereda de persona en la jerarquía de herencia
Autor: Juan Luis Magaña Paz
Fecha: 20 de septiembre de 2019
"""
from persona import persona
class Estudiante(persona):
    # Constructor
    def __init__(self,name,ap,sex,carr,esc,nctrol):
        #Invocamos el constructor de la superclase
        persona.__init__(self,name, ap,sex)
        #Agregamos los atributos de esta clase: Estudiante
        self.carrera = carr
        self.escuela = esc
        self.control = nctrol
    
    #Lista de métodos get
    def getName(self):
        return self.nombre
    def getLastName(self):
        return self.apellidos
    def getSexo(self):
        return self.Sexo
    #Lista de métodos set
    def setCarrera(self,carr):
        self.carrera=carr
    def setEscuela(self, esc):
        self.escuela=esc 
    def setNumControl(self,nctrol):
        self.control=nctrol
    def printTLN(self):
        return persona.personaToString(self)+" "+self.escuela+","+self.carrera+","+self.control
    