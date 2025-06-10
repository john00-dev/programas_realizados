'''
Después de 2 segundos, el script enfoca la pestaña de Chrome llamada “Nueva pestaña” y 
escribe “Este es el nuevo contenido de la página.” pulsando Enter para sobrescribir su contenido.
'''

import pygetwindow as gw
import pyautogui
import time

# Espera unos segundos para que tengas tiempo de enfocarte en la pestaña que quieres sobrescribir
time.sleep(5)

# Encuentra la ventana del navegador Chrome por su título (ajusta el título según tu configuración)
chrome_window = gw.getWindowsWithTitle('Nueva pestaña')[0]

# Cambia el enfoque a la ventana de Chrome
chrome_window.activate()

# Realiza acciones en la pestaña activa usando pyautogui
pyautogui.write('Este es el nuevo contenido de la página.')
pyautogui.press('enter')

# Puedes agregar más interacciones utilizando pyautogui según tus necesidades

# Por ejemplo, si necesitas hacer clic en un botón, puedes hacer algo como:
# pyautogui.click(x, y)

# Recuerda ajustar las coordenadas (x, y) según las ubicaciones donde deseas hacer clic.

# Ten en cuenta que este enfoque puede ser frágil y depende de las coordenadas de la pantalla.
# Si las coordenadas cambian o si hay variaciones en la interfaz, este código puede no funcionar correctamente.
