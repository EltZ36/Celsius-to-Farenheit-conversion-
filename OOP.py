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
    return f'{self.degrees} degrees {self.kind} converts to degrees.'
  
class Kelvin(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def __repr__(self):
    return f'{self.degrees} degrees {self.kind} converts to degrees.'

Temp1 = Fahrenheit(15, "Fahrenheit")
print(Temp1)
  
def Setup():
  print("Welcome to the Temperature converter!")
  Rep = input("What conversion do you want to do? Fahrenheit to Celsius (1), Celsius to Fahrenheit (2), or Celsius to Kelvin (3)?"
  if Rep == 1:
   return None
  elif Rep == 2:
   return None
  elif Rep == 3:
   return None
  else:
    Setup()
Setup()
