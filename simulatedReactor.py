import time
import os
import random

#This class simulates a reactor. It used by the controller for testing purposes. 
#This class never communicates with the user. All communications must be done through the controller.
#Some "events" can happen randomly. It is up to the controller to both detect and respond to events.
class simulatedReactor: 
  temperature = 0.0             #Read Only
  pressure = 0                  #Read/Write
  current = 0                   #Read Only
  voltage = 0                   #Read/Write
  externalNeutronCount = 0      #Read Only
  deuterium = 0                 #Read/Write

  doEvents = False              #Changing this will allow for random events

  def __init__(self):
    self.pressure = 760         #Normal pressure at sea level in torr?
    self.temperature = 20.0     #Room temp in c.
    self.externalNeutronCount = 0 #Count per minute (CPM).

  #This function sets the pressure to a given value.
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

  #This function sets the voltage to a given value.
  def setVoltage(self, n):
    self.displayInfo()
    if self.voltage != n:
      time.sleep(1)
      self.voltage = n
      self.displayInfo()
    else:
      print("ERROR")

  def update(self):
    if self.doEvents == True:
      self.causeRandomEvent()

    #Totally random relationship between temperature and pressure.
    self.temperature = (self.pressure/760)*20 
    #Another random relationship between voltage and current.
    self.current = 3 * self.voltage - 0.05
    #Another uncertian relationship between Neutrons and Voltage
    self.externalNeutronCount = (self.voltage/5)*10

  def displayInfo(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    #This is only for testing purposes. The controller will need to get and print this data. 
    self.update()
    print("---Reactor Info---")

    print("Temperature: ", self.temperature, "C")
    print("Pressure: ", self.pressure, "Torr")
    print("Current: ", self.current, "AMPS")
    print("Voltage: ", self.voltage, "kV")
    print("External Neutron Count: ", self.externalNeutronCount, "CPM")

  def causeRandomEvent(self):
    events = ["vaccumLeak", "currentSurge", "powerEnd"]
    rand = random.randrange(0,500,1)
    if rand == 1:
      randEventName = random.randrange(0,2,1)
      self.event(events[randEventName])

  #These will simulate potential events that could happen.
  #It will be up to the controller to react and respond. 
  def event(self, name):
    if name == "VacuumLeak":
      print("EVENT: Vacuum Leak")
      rand = random.randrange(10,50,1)
      self.pressure -= rand
    elif name == "currentSurge":
      print("EVENT: Surge in current")
      rand = random.randrange(0,20,1)
      self.voltage += rand
    elif name == "powerEnd":
      print("EVENT: Sudden Power Loss")
      self.voltage = 0
    self.displayInto()