"""
En este segundo ejercicio, 
1. tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables,
2. también debe de tener un label con el texto que queráis.
"""

import tkinter
from tkinter import ttk

ventana = tkinter.Tk()
ventana.title("Ejercicio 2")
ventana.geometry("300x300")

opcion_seleccionada = tkinter.StringVar()

def mostrar_pais():
    pais = opcion_seleccionada.get()
    print(pais)

valores = ["Chile", "España", "Brasil"]
combo = ttk.Combobox(ventana, values=valores, textvariable=opcion_seleccionada, state="readonly")
combo.current(0)


etiqueta = tkinter.Label(ventana, text="Selecciona un pais")

etiqueta.pack()
combo.pack()


ventana.mainloop()