'''
Goals:
-Have more options
-Make code much more clean
'''

class Temperature:
  def __init__(self, degrees, kind):
    self.degrees = degrees
    self.kind = kind
  def input(self):
    Player_input = int(input("How many degrees?"))
    self.degrees = Player_input

class Fahrenheit(Temperature):
  def __init__(self, degrees, kind):
    #using super function to call the init (initialization) function of the temperature class.
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
     x = ((9/5 * (self.degrees-273.15))+32) 
    return f'{self.degrees} degrees {self.kind} converts to degrees.'

def Repeat():
 Re1 = input("Do you want to convert again? (Y) or (N)")
 if Re1 == Y:
   Setup()
 else:
   return None

def Setup():
  print("Welcome to the Temperature converter!")
  Response = "What conversion do you want to do? \nFahrenheit to Celsius (1) \nCelsius to Fahrenheit (2) \nKelvin to Fahrenheit  (3)"
  print(Response)
  Temp1 = Fahrenheit(0, "Fahrenheit")
  Temp2 = Celsius(0, "Celsius")
  Temp3 = Kelvin(0, "Kelvin")
  Temp4 = 0
  Temp5 = 0
  Temp6 = 0
  while True:
   try:
    #using a dictionary to reduce the amount of if statements.
    options ={
    "1":Temp1.F_to_C, "2":Temp2.C_to_F, "3":Temp3.K_to_F, "4":Temp4, "5":Temp5, "6":Temp6
    }  
    choice = input("Select the number of the conversion here: ")
    options[choice]()
    break
   except KeyError:
    print("Sorry, please type in the number of the conversion again")
    continue   
Setup()
