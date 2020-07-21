class Temperature:
  def __init__(self, degrees, kind):
    self.degrees = degrees
    self.kind = kind
    
  def add_degrees(self, degrees):
    self.degrees.append(add_degrees)
  
class Fahrenheit(Temperature):
  def __init__(self, degrees, kind):
    F1 = ((F-32)*(5/9))
    super().__init__(degrees, kind) 
    #the 59 and 63 are placeholders.
    self.C_convert = F1
    self.K_convert = "63"
  
class Celsius(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
    self.F_convert = "59"
    self.K_convert = "63"
    
class Kelvin(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
    self.kind = "Kelvin"
    self.F_convert = "59"
    self.K_convert = "63'
