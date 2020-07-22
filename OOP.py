class Temperature:
  def __init__(self, degrees, kind):
    self.degrees = degrees
    self.kind = kind
  
class Fahrenheit(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind) 
  def __repr__(self):
    #using an F string
    return f'{self.degrees} degrees {self.kind} converts to degrees.'

class Celsius(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def __repr__(self):
    return f'{}.'
  
class Kelvin(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def __repr__(self):
    return f'{}.'

Temp1 = Fahrenheit(15, "Fahrenheit")
print(Temp1)
  
