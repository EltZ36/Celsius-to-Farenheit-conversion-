'''
Goals:
-Have more options
-Make code much more clean
-Make it work
'''
class Temperature:
  def __init__(self, degrees, kind):
    self.degrees = degrees
    self.kind = kind
  def input(self):
    Player_input = int(input("How many degrees?")
    self.degrees = Player_input
class Fahrenheit(Temperature):
  def __init__(self, degrees, kind):
    #using super function. Can't really explain what it does. 
    super().__init__(degrees, kind) 
  def __repr__(self):
    self.input() 
    # Fahrenheit to Celsius 
    x = (((self.degrees -32) * 5) /9)
    #using an F string
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'

class Celsius(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def __repr__(self):
    self.input()
    # Celsius to Fahrenheit
    x = (((self.degrees / 5) * 9)  + 32)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
  
class Kelvin(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def __repr__(self):
    self.input()
    # Kelvin to Fahrenheit
    x = ((9/5 * self.degrees)+32) 
    return f'{self.degrees} degrees {self.kind} converts to degrees.'
  
def Setup():
  print("Welcome to the Temperature converter!")
  Rep = int(input("What conversion do you want to do? Fahrenheit to Celsius (1), Celsius to Fahrenheit (2), or Celsius to Kelvin (3)?")
  if Rep == 1:
   y = 0
   Repeat()         
  elif Rep == 2:
   y = 0
   Repeat()
  elif Rep == 3:
   y = 0
   Repeat()         
  else:
    Setup()
Setup()

def Repeat():
 Re1 = input("Do you want to convert again? (Y) or (N)")
 if Re1 == Y:
   Setup()
 else:
   Return None
