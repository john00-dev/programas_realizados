'''

Este script obtiene una lista de todas las ventanas 
abiertas en el sistema y las imprime.

'''
import pygetwindow as gw

# Obtiene una lista de todas las ventanas abiertas
windows_list = gw.getAllTitles()

# Imprime los títulos de las ventanas
print(windows_list)