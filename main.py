def C_to_F():
  c = int(input("How many degrees Centigrade?"))
  F1 = (((c/5)*9)+32)
  print(str(F1) + ' degrees Centigrade')
  Again = input("Do you want to convert again? (Y) or (N)")
  if Again == "Y":
    temperature_convert()
  else:
    return None

def T_to_C():
  f = int(input("How many degrees Fahrenheit?"))
  C1 = (((f-32)*5)/9)
  print(str(C1) + ' degrees Fahrenheit')
  Again2 = input("Do you want to convert again? (Y) or (N)")
  if Again2 == "Y":
    temperature_convert()
  else:
    return None

def temperature_convert():
  Question = int(input("Do you want to convert from Centigrade to Fahrenheit (1) or Fahrenheit to Centigrade? (2)"))
  if Question == 1: 
    Question = True
    while Question == True:
      C_to_F()
      #Break stops the while loop from looping and starting the conversion over again.
      break
  elif Question == 2:
    Question = True
    while Question == True:
      T_to_C()
      break
  else:
    print("Please type in the number next to the conversion that you want.")
    temperature_convert()
print('Welcome!')
temperature_convert()
