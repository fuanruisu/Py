""" 
Nombre: calcu.py
Objetivo: crea calculadora con tkinter
Autor: Juan Luis Magaña Paz
Fecha: 09/Oct/2019
"""
from tkinter import *
from math import *
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("600x600")
ventana.configure(background="#f73e3e")
color_boton=("#ff6363")


def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) #Muestra el operador en la pantalla
    

def clear():
    global operador
    operador=("")
    input_text.set("0")

def operacion():
    global operador
    try:
        opera=str(eval(operador))#visualizar la operacion en la pantalla previamente
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)#resultado en pantalla


    
ancho_boton=10
alto_boton=4
input_text=StringVar()
operador=""
clear() #Limpia la pantalla mostrando 0
Boton0=Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=50,y=440)
Boton1=Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=50,y=180)
Boton2=Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=200,y=180)
Boton3=Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=350,y=180)
Boton4=Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=50,y=260)
Boton5=Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=200,y=260)
Boton6=Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=350,y=260)
Boton7=Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=50,y=350)
Boton8=Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=200,y=350)
Boton9=Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=350,y=350)
BotonC=Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=350,y=520)
BotonComa=Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=200,y=440)
BotonSuma=Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=500,y=260)
BotonResta=Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=500,y=180)
BotonMulti=Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=500,y=350)
BotonDiv=Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=500,y=440)

BotonC=Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=500,y=520)

BotonResul=Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=operacion).place(x=350,y=440)
#declaración de la pantalla
Salida=Entry(ventana,font=('arial',20,'bold'),width=35,textvariable=input_text,bd=20,insertwidth=4,bg="beige",justify="right").place(x=10,y=60)


ventana.mainloop()