import tkinter as tk

def accion_boton():
    print("El boton ha sido presionado")

ventana =tk. Tk()

ventana.title("Activador de Windows")

etiqueta = tk.Label(ventana, text="Presiona el botón")
etiqueta.pack()

boton = tk.Button(ventana, text="Presióname", command=accion_boton)
boton.pack()

ventana.mainloop()