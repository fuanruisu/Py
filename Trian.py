def IdentificaTipoTriean(L1,L2,L3):
    if(L1==L2 and L1==L3):
        print('Triangulo equiaterio',L1,",",L2,',',L3)
    elif(L1 != L2) and (L3 != L1):
        print('Triangulo escaleno',L1,",",L2,',',L3)
    else:
        print('Triangulo osoceles',L1,",",L2,',',L3)

def menu():
    print('--Script para identificar triangulo--')
    #Capturar los lados por el teclado
    L1=int(input('Introduzca el primer lado:'))
    L2=int(input('Introduzca el segundo lado:'))
    L3=int(input('Introduzca el tercer lado:'))
    #Invocamos la funcion
    IdentificaTipoTriean(L1,L2,L3)

def main():
    continuar=True
    while(continuar==True):
        menu()
        print('Desea hacer otro calculo S/N?')
        car= input()
        if(car !='S' or car != 's'):
            continuar=False
    print('Fin del programa')

if __name__=="__main__":
    main()