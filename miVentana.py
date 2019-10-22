""" 
Nombre: miVentana.py
Objetivo: Utiliza la librería tkinter para dibujar en python
Autor: Juan Luis Magaña Paz
Fecha: 04/Oct/2019
"""
from tkinter import*
from tkinter import ttk 

#Creamos una ventana 
v = Tk()
#Modificamos las dimensiones de la ventana
v.geometry('800x800')
v.configure(bg = '#A05733')
#Título de la barra 
v.title("Mi primer ventana en python")
w= Label(v, text="Hello, world!",font=("Comic Sans ms", 14))

w.place(x=500,y=50)
#v.config(width=300, height=200)
# Crear caja de texto.
entry = ttk.Entry(v)
# Posicionarla en la ventana.
entry.place(x=10, y=500)

w.pack()

#Ciclo de espera de la interaccion
v.mainloop()