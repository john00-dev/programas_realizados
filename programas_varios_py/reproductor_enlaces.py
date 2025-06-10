'''
Este script permite abrir enlaces almacenados en un archivo JSON a través de una interfaz gráfica.(tik tik)
El usuario puede ingresar un número para abrir un enlace específico, o navegar entre enlaces con botones.
'''

import json
import webbrowser
import tkinter as tk

# Leer el archivo JSON con la codificación utf-8
with open('archivo.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

# Obtener la lista de enlaces
lista_enlaces = datos["Activity"]["Like List"]["ItemFavoriteList"]
total_enlaces = len(lista_enlaces)
indice_actual = total_enlaces - 1  # Comenzar desde el último enlace

# Función para abrir el enlace correspondiente al número ingresado
def abrir_enlace_personalizado():
    try:
        numero_enlace = int(entrada_enlace.get()) - 1  # Restar 1 para ajustar al índice de la lista
        if 0 <= numero_enlace < total_enlaces:
            enlace_personalizado = lista_enlaces[numero_enlace]["Link"]
            webbrowser.open(enlace_personalizado)
            etiqueta.config(text=f"Abriendo enlace {numero_enlace + 1} de {total_enlaces}")
        else:
            etiqueta.config(text="Número de enlace inválido")
    except ValueError:
        etiqueta.config(text="Por favor, ingresa un número válido")

# Función para reproducir el enlace anterior
def reproducir_anterior():
    global indice_actual
    if indice_actual > 0:
        indice_actual -= 1
        abrir_enlace()

# Función para reproducir el enlace siguiente
def reproducir_siguiente():
    global indice_actual
    if indice_actual < total_enlaces - 1:
        indice_actual += 1
        abrir_enlace()

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Reproductor de Enlaces")

# Barra para ingresar el número del enlace de la lista
entrada_enlace = tk.Entry(ventana, width=50)
entrada_enlace.pack(pady=10)
boton_enlace_personalizado = tk.Button(ventana, text="Abrir Enlace Personalizado", command=abrir_enlace_personalizado)
boton_enlace_personalizado.pack()

# Etiqueta para mostrar el número del enlace actual
etiqueta = tk.Label(ventana, text=f"Abriendo enlace {indice_actual + 1} de {total_enlaces}")
etiqueta.pack()

# Botones para reproducir enlace anterior y siguiente
boton_anterior = tk.Button(ventana, text="Anterior", command=reproducir_anterior)
boton_anterior.pack(side=tk.LEFT)
boton_siguiente = tk.Button(ventana, text="Siguiente", command=reproducir_siguiente)
boton_siguiente.pack(side=tk.RIGHT)

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()

