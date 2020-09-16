'''
Goals: -More clean and readable code.
-Make the temperature conversions more accurate.
'''

def Repeat():
  while True:
    try:
      Again = input("Do you want to convert again? (Y) or (N)")
      Options = {"Y":temperature_convert, "y":temperature_convert, " y":temperature_convert, "Y":temperature_convert, "N":exit, "n":exit}
      print(Options[Again]())
    #Keyerror occurs when the input/key isn't found in the dictionary.
    except KeyError:
      print("Try to enter (Y) or (N) again.")
      Repeat()

#Fahrenheit to Celsius, Kelvin, and Rankine conversions
def F_to_C():
  f = float(input("How many degrees Fahrenheit?"))
  C1 = ((f - 32) * (5/9))
  # Have to convert this(C1) into a string as it is a float and can't be added with another string.
  print(str(C1) + ' degrees Fahrenheit')
  Repeat()
  
def F_to_K():
  f2 = float(input("How many degrees Fahrenheit?"))
  K2 = (((f2 -32) * 5/9) + 273.15)
  print(str(K2) + ' degrees Kelvin')
  Repeat()

def F_to_R():
  f3 = float(input("How many degrees Fahrenheit?"))
  R3 = (f3 + 459.67)
  print(str(R3) + ' degrees Rankine')
  Repeat()

#Celsius to Fahrenheit, Kelvin, and Rankine conversions
def C_to_F():
  # float allows for both integers and decimals.
  c = float(input("How many degrees Centigrade?"))
  F1 = (c *(9/5) + 32)
  print(str(F1) + ' degrees Centigrade')
  Repeat()

def C_to_K():
  c2 = float(input("How many degrees Centigrade?"))
  K = (c2 + 273.15)
  print(str(K) + " degrees Kelvin")
  Repeat()

def C_to_R():
  c3 = float(input("How many degrees Celsius"))
  R2 = (((c3) * 9/5 ) + 491.67)
  print(str(R2)+" degrees Rankine")
  Repeat()
  

#Kelvin to Celsius, Fahrenheit, and Rankine conversions
def K_to_C():
  k1 = float(input("How many degrees Kelvin?"))
  C2 = (k1 - 273.15)
  print(str(c2) + " degrees Celsius")
  Repeat()

def K_to_F():
  k2 = float(input("How may degrees Kelvin?"))
  F2 = (((k2 - 273.15) * 9/5) + 32) 
  print(str(F2) + " degrees Kelvin")
  Repeat()

def K_to_R():
  k3 = float(input("How many degrees Kelvin?"))
  R3 = (k3 * 1.8)
  print(str(R3)+" degrees Rankine")
  Repeat()
  
#Rankine to Kelvin, Celsius, and Temperature conversions  
def R_to_F():
  r1 = (float(input("How many degrees Rankine?")))
  F3 = r1 - 459.67
  print(str(F3)+" degrees Fahrenheit")
  Repeat()

def R_to_C():
  r2 = (float(input("How many degrees Rankine?")))
  C3 = ((r2 - 491.67) * 5/9)
  print(str(C3)+" degrees Celsius")
  Repeat()

def R_to_K():
  r3 = (float(input("How many degrees Rankine?")))
  K3 = (r3 * 5/9)
  print(str(K3)+" degrees Kelvin")
  Repeat()

def temperature_convert():
 # Lines 55 - 70 check if the input is correct and if it is, then it will convert the temperature. Otherwise if the input(key) isn't found, the while loop will continue.
  Question = """Which conversion do you want?
  \n- Centigrade to Fahrenheit (1) - Fahrenheit to Centigrade(2) \n- Centigrade to Kelvin (3) - Fahrenheit to Kelvin (4) 
  \n-Kelvin to Centigrade (5) - Kelvin to Fahrenheit (6) 
  \n- Fahrenheit to Rankine (7) - Celsius to Rankine (8) - Kelvin to Rankine (9) 
  \n- Rankine to Fahrenheit (10) -Rankine to Celsius (11) -Rankine to Kelvin (12)
  """
  print(Question)
  while True:
   try:
    options ={
    "1":C_to_F, "2":F_to_C, "3":C_to_K, '4':F_to_K, '5':K_to_C, '6':K_to_F, '7':F_to_R , 
    '8':C_to_R, '9':K_to_R, '10':R_to_F, '11':R_to_C, '12':R_to_K
    }  
    choice = input("Select the number of the conversion here: ")
    print(options[choice]())
    break
   except KeyError:
    print("Sorry, please type in the number of the conversion again")
    continue 
print('Welcome to the Temperature Converter!')
temperature_convert()
