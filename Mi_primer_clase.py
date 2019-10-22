# Nombre: Mi_primer_clase.py
# Objetivo: Muestra como crear clases en python
# Autor: Juan Luis Magaña Paz
# Fecha: 13 de septiembre de 2019

class Punto():
    # Método "constructor", este método
    # Permite construir objetos en la memoria de la PC
    def __init__(self, px, py):
     #Atributods x,y
        self.x=px
        self.y=py
    # Métodos get para regresar los atributos de un objeto
    def getAtributos(self):
        return self.x ,self.y 
    def setAtributos(self, valorX,valorY):
        self.x=valorX
        self.y=valorY
    # Método para calcular la distancia entre dos puntos
    # distancia entre dos puntos d=sqr(p2.x-p1.x1)pow2+(p2.y-p1.x1)
    def distancia(self, self):
        dist=math.sqrt(math.pow(a2.x-a1.x),2)+math.pow((a2.y-a1.y),2)
        return dist

def main():
    # Construir objetos de la clase
    # Una clase es una productora de objetos del mismo tipo 
    p1=Punto(3,1)
    p2=Punto(4,10)
    p3=Punto(-5,-10)
    p4=Punto(12,31)
    
    # Imprimir los atributos de cada objeto
    print("Objeto P1", p1.getAtributos())
    print("Objeto P2", p2.getAtributos())
    print("Objeto P3", p3.getAtributos())
    print("Objeto P4", p4.getAtributos())
    p1.setAtributos(-3,-1)
    p2.setAtributos(-4,-10)
    p3.setAtributos(5,10)
    p4.setAtributos(-12,-31)
    print("Objeto P1", p1.getAtributos())
    print("Objeto P2", p2.getAtributos())
    print("Objeto P3", p3.getAtributos())
    print("Objeto P4", p4.getAtributos())
    
if __name__ == "__main__":
    main()