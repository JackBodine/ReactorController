class simulatedReactor: 
  temperature = 0
  pressure = 0
  current = 0

  def __init__(self):
    self.pressure = 760,000   #This is the avg. pressure in microns at sea level.
    self.temperature = 20     #Room temp in c.
