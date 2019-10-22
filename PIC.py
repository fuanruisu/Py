"""
Nombre: PIC.py
Objetivo: Construye objetis tipo PIC
Autor: Juan Luis Magaña Paz
Fecha: 17 de septiembre de 2019
"""
import os
class PIC():
    #Constructor: instancia la clase para construir objetos
    def __init__(self,code, name, model, dp, ap, pp, mem, price):
        os.system("cls")
        print("--Creando nuevo objeto--")
        self.clave = code
        self.marca = name
        self.modelo = model
        self.digitalPort = dp 
        self.analogPort = ap
        self.powerport = pp 
        self.memory = mem
        self.precio = price
    # Lista de métodos get: regresan valor de atributos
    def getClave(self):
        return self.clave
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getdigitalPort(self):
        return self.digitalPort
    def getanalogPort(self):
        return self.analogPort
    def getpowerport(self):
        return self.powerport
    def getmemory(self):
        return self.memory
    def getprecio(self):
        return self.precio
    #Lista de métodos set: modificamos atributos del objeto
    def setClave(self, code):
        self.clave = code
    def setMarca(self, name):
        self.clave = name
    def setModelo(self, model):
        self.modelo = model
    def setdigitalPort(self, dp):
        self.digitalPort = dp
    def setanalogPort(self, ap):
        self.analogPort = ap
    def setpowerport(self, pp):
        self.powerport = pp
    def setmemoria(self, mem):
        self.memory = mem
    def setprecio(self, price):
        self.precio = price
    def printAtributos(self):
        #Invocar métodos get
        print("Clave:",self.getClave(),"\n",
        "Marca:",self.getMarca(),"\n",
        "Modelo:",self.getModelo(),"\n",
        "GPIO:",self.getdigitalPort(),"\n",
        "A/D:",self.getanalogPort(),"\n",
        "Powerport",self.getpowerport(),"\n",
        "Memoria:",self.getmemory(),"\n",
        "Precio:",self.getprecio(),"\n",)