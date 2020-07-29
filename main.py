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
  C2 = float(input("How many degrees Centigrade?"))
  K = (C2 + 273.15)
  print(str(K) + " degrees Kelvin")
  Repeat()
  
def K_to_C():
  k1 = float(input("How many degrees Kelvin?"))
  C = (k1 -273.15)
  print(str(C) + " degrees Celsius")
  Repeat()
  
def temperature_convert():
  #Checks if the question option is not a float or another word. The else statement at lines 52-54 makes sure that the person can type in the number again if they make a mistake.
  while True:
    try:
      #\n indicates the end of a line and prints the code next to the \n on another line.
       Question = int(input("Which conversion do you want?\nCentigrade to Fahrenheit (1) \nFahrenheit to Centigrade(2) \nCentigrade to Kelvin (3) \nFahrenheit to Kelvin (4) \nKelvin to Centigrade (5)"))
    except ValueError:
        print("Please type in the number conversion you want again.")
        continue
    else:
      # breaks the while loop and makes the loop not occur again.
      break
  if Question == 1: 
    #Nested Function and not recursion.
    C_to_F()
  elif Question == 2:
    F_to_C()
  elif Question == 3:
    C_to_K()
  elif Question == 4:
    F_to_K()
  elif Question == 5:
    K_to_C()
  else:
    print("Please type in the number next to the conversion you want.")
    # Guess this is a form of recursion where the function calls itself again.
    temperature_convert()

print('Welcome to the Temperature Converter!')
temperature_convert()
