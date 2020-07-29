'''
Goals: -More options
-More clean and readable code.
-Try to make sure if people use this, that there is an int check. 
'''

def Repeat():
  Again = input("Do you want to convert again? (Y) or (N)")
  if Again == "Y":
    temperature_convert()
  return None

def C_to_F():
  c = int(input("How many degrees Centigrade?"))
  F1 = ( ( (c/5) * 9 ) + 32)
  print(str(F1) + ' degrees Centigrade')
  Repeat()

def F_to_C():
  f = int(input("How many degrees Fahrenheit?"))
  C1 = ( ( (f - 32) * 5) /9)
  # Have to convert C1 to a string as it is a float and can't be added with another string.
  print(str(C1) + ' degrees Fahrenheit')
  Repeat()

def C_to_K():
  C2 = int(input("How many degrees Centigrade?"))
  K = (C2 + 273.15)
  print(str(K) + " degrees Kelvin")
  Repeat()
  
def K_to_C():
  k1 = int(input("How many degrees Kelvin?"))
  C = (k1 -273.15)
  print(str(C) + " degrees Celsius")
  Repeat()
  
def temperature_convert():
  Question = int(input("Do you want to convert from Centigrade to Fahrenheit (1) , Fahrenheit to Centigrade? (2), Centigrade to Kelvin? (3) or Kelvin to Centigrade? (4)"))
  if Question == 1: 
    Question = True
    while Question == True:
      #Nested Function and not recursion.
      C_to_F()
      #Break stops the while loop from looping and starting the conversion over again.
      break
  elif Question == 2:
    Question = True
    while Question == True:
      F_to_C()
      break
  elif Question == 3:
    Question = True
    while Question == True:
      C_to_K()
      break
  elif Question == 4:
    Question = True
    while Question == True:
      K_to_C()
      break
  else:
    print("Please type in the number next to the conversion you want.")
    # Guess this is a form of recursion where the function calls itself again.
    temperature_convert()

print('Welcome to the Temperature Converter!')
temperature_convert()
