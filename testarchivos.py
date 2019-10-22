import random

def crearArchivo():
    myfile=open("myarchivo.txt","w")
    for i in range(1,10):
        myfile.write(str(i)+",")

def temp():
    d=random.randrange(10,99,1)
    return d

def main():
    crearArchivo()

if __name__ == "__main__":
    main()