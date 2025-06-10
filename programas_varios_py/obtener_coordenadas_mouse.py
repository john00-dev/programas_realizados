'''

Este script obtiene las coordenadas del puntero del ratón y las imprime en la consola.

'''
import pyautogui
import time

# Espera 10 segundos antes de ejecutar el código (puedes ajustar este tiempo según sea necesario)
time.sleep(10)

# Obtiene y muestra las coordenadas del puntero del ratón
x, y = pyautogui.position()
print(f"Coordenadas del ratón: X={x}, Y={y}")
