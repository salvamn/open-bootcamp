import tkinter

ventana = tkinter.Tk()
ventana.title("Ejercicio 1")
ventana.geometry("300x400")

opcion = tkinter.IntVar()
etiqueta = tkinter.Label(ventana, text="Selecciona una opcion")


def mostrar_opcion_selecionada():
    etiqueta["text"] = opcion.get()
    
def reiniciar():
    etiqueta["text"] = "Seleccione una opcion"
    opcion.set(0)


radio1 = tkinter.Radiobutton(ventana, text="Opcion 1", variable=opcion, value=1, command=mostrar_opcion_selecionada)
radio2 = tkinter.Radiobutton(ventana, text="Opcion 2", variable=opcion, value=2, command=mostrar_opcion_selecionada)
radio3 = tkinter.Radiobutton(ventana, text="Opcion 3", variable=opcion, value=3, command=mostrar_opcion_selecionada)

btn_reiniciar = tkinter.Button(ventana, text="Reiniciar", command=reiniciar)

radio1.pack()
radio2.pack()
radio3.pack()
etiqueta.pack()
btn_reiniciar.pack()


ventana.mainloop()