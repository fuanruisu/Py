"""
Nombre: ventana.py
Objetivo: Muestra como construir interfaces gráficas con la librería tkinter
Autor: Alumnos de mecatrónica
Fecha:08/Oct/2019
"""
#importamos libreria tkinter
from tkinter import*
#Construir una ventana raiz
vent = Tk()
#Modificar propiedades a la ventana
mf=Frame(vent)
vent.geometry('500x350')
vent.configure(background='#1560bd')
#Campo de texto, pantalla de la calculadora
frame = Frame(vent) 
frame.pack() 
frame.config(bg="red")
#frame.config(width=500,height=320)  
minusb= Button(frame, text="-", fg="black")
minusb.pack(side="bottom",ipadx=12,ipady=10)
plusb= Button(frame, text="+", fg="black")
plusb.pack( side="bottom",ipadx=11,ipady=10)
Nine= Button(frame, text="9", fg="black")
Nine.pack(side="left",ipadx=12,ipady=10)
Eight= Button(frame, text="8", fg="black")
Eight.pack( side="left",ipadx=11,ipady=10)
sc = Entry(vent,width=30)
sc.place(x=100, y=50)
#ciclo de captura de eventos
vent.mainloop()