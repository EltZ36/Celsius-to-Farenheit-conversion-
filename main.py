'''
Goals: -More options
-More clean and readable code.
-Less if statements.
-Try to make sure if people use this, that there is an int check. 
-Make the temperature conversions more accurate.
-Reorder the conversions.
'''

def Repeat():
  Again = input("Do you want to convert again? (Y) or (N)")
  if Again == "Y" or Again == " Y":
    temperature_convert()
  return None

def C_to_F():
  # float allows for both integers and decimals
  c = float(input("How many degrees Centigrade?"))
  F1 = ( ( (c/5) * 9 ) + 32)
  print(str(F1) + ' degrees Centigrade')
  Repeat()

def F_to_C():
  f = float(input("How many degrees Fahrenheit?"))
  C1 = ( ( (f - 32) * 5) /9)
  # Have to convert this(C1) into a string as it is a float and can't be added with another string.
  print(str(C1) + ' degrees Fahrenheit')
  Repeat()
  
def F_to_K():
  f2 = float(input("How many degrees Fahrenheit?"))
  K2 = ((((f2 -32) * 5) /9) +273.15)
  print(str(K2) + ' degrees Kelvin')
  Repeat()

def C_to_K():
  c2 = float(input("How many degrees Centigrade?"))
  K = (c2 + 273.15)
  print(str(K) + " degrees Kelvin")
  Repeat()
  
def K_to_C():
  k1 = float(input("How many degrees Kelvin?"))
  C2 = (k1 -273.15)
  print(str(c2) + " degrees Celsius")
  Repeat()

def K_to_F():
  k2 = float(input("How may degrees Kelvin?"))
  F2 = (((k2 - 273.15) * 9/5) + 32) 
  print(str(F2) + " degrees Kelvin")
  Repeat()

def temperature_convert():
 # Lines 55 - 70 check if the input is correct and if it is, then it will convert the temperature. Otherwise if the input(key) isn't found, the while loop will continue.
  Question = "Which conversion do you want?\nCentigrade to Fahrenheit (1) \nFahrenheit to Centigrade(2) \nCentigrade to Kelvin (3) \nFahrenheit to Kelvin (4) \nKelvin to Centigrade (5) \nKelvin to Fahrenheit (6)"
  print(Question)
  while True:
   try:
    #using a dictionary to reduce the amount of if statements.
    options ={
    "1":C_to_F, "2":F_to_C, "3":C_to_K, '4':F_to_K, '5':K_to_C
    }  
    choice = input("Select the number of the conversion here: ")
    options[choice]()
    break
   except KeyError:
    print("Sorry, please type in the number of the conversion again")
    continue 
print('Welcome to the Temperature Converter!')
temperature_convert()
