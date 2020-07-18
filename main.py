def temperature_convert():
  Question = int(input("Do you want to convert from Centigrade to Fahrenheit (1) or Fahrenheit to Centigrade? (2) "))
  if Question == 1:
    Question = True
    while Question == True:
    c = int(input("How many degrees Centigrade?"))
    F1 = (((c/5)*9)+32)
    print(str(F1) + ' degrees Centigrade')
    break
  elif Question == 2:
   Question = True
   while Question == True:
      f = int(input("How many degrees Fahrenheit?"))
      return f
  else:
    print("Please enter the number next to the option you want.")
    temperature_convert()
temperature_convert()
