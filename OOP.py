class Temperature:
  def __init__(self, degrees, kind):
    self.degrees = degrees
    self.kind = kind
  
class Fahrenheit(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind) 
    #the 59 and 63 are placeholders.
  def __repr__(self):
    C1 = (((self.degrees -32)*5)/9)
    return C1 
Temp1 = (15, "Fahrenheit")
print(Temp1)
  
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
