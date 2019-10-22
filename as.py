import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(width=300, height=200)
# Crear caja de texto.
entry = ttk.Entry(root)
# Posicionarla en la ventana.
entry.place(x=100, y=50)
root.mainloop()