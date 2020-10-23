import time
import os

def test(): 
  myReactor = simulatedReactor
  myReactor.setPressure(500000)

class simulatedReactor: 
  temperature = 0.0
  pressure = 0
  current = 0

  def __init__(self):
    self.pressure = 760         #Normal pressure at sea level in torr?
    self.temperature = 20.0     #Room temp in c.

  def setPressure(self, n):
    self.displayInfo()
    if self.pressure == n:
      return True
    elif self.pressure > n:
      self.pressure -= 10
      time.sleep(1)
      self.setPressure(n)
    elif self.pressure < n:
      self.pressure += 10
      time.sleep(1)
      self.setPressure(n)
    else:
      print("ERROR")

  def setCurrent(self, n):
    self.displayInfo()
    if self.current != n:
      time.sleep(1)
      self.current = n
      self.displayInfo()
    else:
      print("ERROR")

  def updateTemp(self):
    #Totally random relationship between temperature and pressure.
    self.temperature = (self.pressure/760)*20 

  def displayInfo(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    #This is only for testing purposes. The controller will need to get and print this data. 
    self.updateTemp()
    print("Reactor Temperature: ", self.temperature)
    print("Reactor Pressure: ", self.pressure)
    print("Reactor Current: ", self.current)