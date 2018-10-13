'''
    File name: main.py
    Author: Cesar Cruz
    Date created: 9 OCT 2018    
    Python Version: 2.7
'''

from Tkinter import *
from threading import Thread
from Arduino_Bluetooth import Arduino_Bluetooth
import time

MAC_ADDRESS = '98:D3:32:31:26:4E'
comunicacion_bluetooth = Arduino_Bluetooth() # Clase auxiliar para la comunicacion con Arduino


def adquisicion_Datos(label_pulso):  
  global comunicacion_bluetooth
  comunicacion_bluetooth.set_mac_address(MAC_ADDRESS)
  comunicacion_bluetooth.connectBT()
  comunicacion_bluetooth.sendData('X')

  while True:
    nuevo_dato = comunicacion_bluetooth.receiveData()
    
    if nuevo_dato is not None:
      print "Nuevo dato: " + str(nuevo_dato.isdigit())
      dato = int(nuevo_dato)
      color = "red"
      
      print 'dato -> ' + str(dato) + "->" + str(type(dato))
      if (dato >= 60 and dato <= 90):
        color = "green"    

      label_pulso.config(text=dato, fg=color)
      label_pulso.text = dato
    else:
      break

    # time.sleep(1)

def on_closing():
  global comunicacion_bluetooth  
  comunicacion_bluetooth.closeConnection()
  root.destroy()

# Configuracion de la GUI
root = Tk()
root.title('Pulso cardiaco')
root.geometry("300x100") 

# Se crea el Label que contendra los datos recibidos
pulso_cardiaco = Label(root, text='29', font=('FreeMono', 100))
pulso_cardiaco.pack()

# Se crea el hilo que estara leyendo los datos
proceso_adquisicion = Thread(target=adquisicion_Datos, args=(pulso_cardiaco, ))
proceso_adquisicion.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
