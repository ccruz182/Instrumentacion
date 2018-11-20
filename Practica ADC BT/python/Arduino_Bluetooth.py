'''
    File name: main.py
    Author: Cesar Cruz
    Date created: 10 OCT 2018    
    Python Version: 2.7
'''

import bluetooth

ERROR_STR = 'Something went wrong -> '
class Arduino_Bluetooth:
  mac_address = ""
  port = 1
  socket = None

  def set_mac_address(self, mac_address):
    self.mac_address = mac_address

  def connectBT(self):
    self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try: 
      self.socket.connect((self.mac_address, self.port))
      print 'Connection established!'
    except IOError, exc:
      print ERROR_STR + str(exc)

  def sendData(self, data):
    try: 
      self.socket.send(str(data))
    except IOError, exc:
      print ERROR_STR + str(exc)  

  def receiveData(self):
    try:       
      recDa = "a"
      rcvDat = ""

      while ord(recDa) != 10:
        recDa = self.socket.recv(1)            
        rcvDat += recDa
        # print rcvDat
      
      print rcvDat
      return rcvDat
    except IOError, exc:
      print  ERROR_STR + str(exc)      

  def closeConnection(self):
    print 'Closing socket'
    try:
      self.socket.close()
      print 'Socket closed! Bye'
    except IOError, exc:
      print  ERROR_STR + str(exc)
