""" 
Nombre: miVentana.py
Objetivo: Utiliza la librería tkinter para dibujar en python
Autor: Juan Luis Magaña Paz
Fecha: 05/Oct/2019
"""
import tkinter as tk 
ventana=tk.Tk()
ventana.title("Primer ventana")
#Anchoxalto
ventana.geometry('380x300')
ventana.configure(background='#1560bd')
etiqueta1=tk.Label(ventana,text="Que tranza raza",bg="White",fg="#100c08")
etiqueta1.pack(side=tk.LEFT)
etiqueta2=tk.Label(ventana,text="Que transita por sus venas",bg="#ffdf00",fg="#100c08")
etiqueta2.pack(padx=20,pady=5,ipadx=20,ipady=20,side=tk.LEFT)
ventana.mainloop()