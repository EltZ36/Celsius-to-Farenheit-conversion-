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
  def Repeat():
    Re1 = input("Do you want to convert again? (Y) or (N)")
    if Re1 == Y:
      Setup()
    else:
      return None

class Fahrenheit(Temperature):
  def __init__(self, degrees, kind):
    #using super function to call the init (initialization) function of the temperature class.
    super().__init__(degrees, kind) 
  def F_to_C(self):
    self.input() 
    # Fahrenheit to Celsius 
    x = (((self.degrees -32) * 5) /9)
    #using an F string
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
  def F_to_K(self):
    self.input()
    # Fahrenheit to Kelvin 
    x = ((((self.degrees-32)*5)/9)+273.15)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
  def F_to_R(self):
    self.input()

class Celsius(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def C_to_F(self):
    self.input()
    # Celsius to Fahrenheit
    x = (((self.degrees / 5) * 9)  + 32)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
  def C_to_K(self):
    self.input()
    # Celsius to Kelvin 
    x = ( self.degrees + 273.15)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
  def C_to_R(self):
    self.input()

class Kelvin(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def K_to_F(self):
    self.input()
    # Kelvin to Fahrenheit
    x = ((9/5 * (self.degrees-273.15))+32) 
    return f'{self.degrees} degrees {self.kind} converts to degrees.'
  def K_to_C(self):
    self.input()
    x = (self.degrees - 273.15)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
  def K_to_R(self):
    self.input()

class Rankine(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def R_to_F(self):
    self.input()
  def R_to_C(self):
    self.input()
  def R_to_K(self):
    self.input()

def Setup():
  print("Welcome to the Temperature converter!")
  Response = """What conversion do you want to do? \nFahrenheit to Celsius (1) \nFahrenheit to Kelvin (2) \nCelsius to Fahrenheit (3) 
  \nCelsius to Kelvin (4) \nKelvin to Fahrenheit (5) \nKelvin to Celsius (6)
  """
  print(Response)
  Temp1 = Fahrenheit(0, "Fahrenheit")
  Temp2 = Fahreneheit(0, "Fahrenheit")
  Temp3 = Celsius(0, "Celsius")
  Temp4 = Celsius(0, "Celsius")
  Temp5 = Kelvin(0,"Kelvin")
  Temp6 = Kelvin(0,"Kelvin")
  while True:
   try:
    #using a dictionary to reduce the amount of if statements.
    options ={
    "1":Temp1.F_to_C, "2":Temp2.F_to_K, "3":Temp3.C_to_F, "4":Temp4.C_to_K, "5":Temp5.K_to_F, "6":Temp6.K_to_C
    }  
    choice = input("Select the number of the conversion here: ")
    options[choice]()
    break
   except KeyError:
    print("Sorry, please type in the number of the conversion again")
    continue   
Setup()
