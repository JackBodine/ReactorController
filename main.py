from simulatedReactor import simulatedReactor

isOn = False

simulatedReactor = simulatedReactor()

#Data to get from sensors:
TEMPERATURE = 0
CURRENT = 0
PRESSURE = 0

def main(): 
  #Displays GUI

  while(isOn):
    print('looped')
    #Listen for button presses/controls
    #Updates GUI
    #Regulatory 

  return True

#Attempts to change pressure by a set amount n.
def changePressure(n):
  #TODO
  return n

#Attempts to start the reactor.
#Returns True if successful
def startup():
  global isOn
  isOn = True
  #TODO
  return True

#Attempts to shutdown the reactor.
#Returns True if successful
def shutdown():
  global isOn
  #TODO
  isOn = False
  return True
