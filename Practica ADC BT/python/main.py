'''
    File name: main.py
    Author: Cesar Cruz
    Date created: 20 NOV 2018    
    Python Version: 2.7
'''

from Tkinter import *
from threading import Thread
import time

from Arduino_Bluetooth import Arduino_Bluetooth
from angulos import get_rango

MAC_ADDRESS = '98:D3:32:31:26:4E'
DELIMITADOR = '&'
V_REF = 5.0
RESOLUCION = V_REF / 255
DEG_SYM = u"\u00b0"
comunicacion_bluetooth = Arduino_Bluetooth() # Clase auxiliar para la comunicacion con Arduino


def adquisicion_Datos(label_temp, label_angulo):  
  global comunicacion_bluetooth
  comunicacion_bluetooth.set_mac_address(MAC_ADDRESS)
  comunicacion_bluetooth.connectBT()
  comunicacion_bluetooth.sendData('X')

  while True:
    nuevos_datos = comunicacion_bluetooth.receiveData()
    
    if nuevos_datos is not None:
      # print "nuevos datos:", nuevos_datos
      # [0] -> temperatura, [1] -> angulo
      datos = nuevos_datos.split(DELIMITADOR)
      temperatura = int(datos[0].lstrip().rstrip()) * RESOLUCION
      angulo = int(datos[1].lstrip().rstrip()) * RESOLUCION
      temperatura = round(temperatura * 10, 2);
      
      label_temp.config(text="Temperatura: " + str(temperatura) + " " + DEG_SYM + "C")
      label_temp.text = "Temperatura: " + str(temperatura) + " " + DEG_SYM + "C"

      label_angulo.config(text="Angulo: " + str(angulo))
      label_angulo.text = "Angulo: " + str(angulo)
    else:
      break
    
def on_closing():
  global comunicacion_bluetooth  
  comunicacion_bluetooth.closeConnection()
  root.destroy()

# Configuracion de la GUI
root = Tk()
root.title('ADC0809')
root.geometry("1000x200") 

# Se crean los Label que contendran los datos recibidos
temperatura = Label(root, text='15', font=('FreeMono', 50))
temperatura.pack()
angulo = Label(root, text='15', font=('FreeMono', 50))
angulo.pack()

# Se crea el hilo que estara leyendo los datos
proceso_adquisicion = Thread(target=adquisicion_Datos, args=(temperatura, angulo, ))
proceso_adquisicion.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
