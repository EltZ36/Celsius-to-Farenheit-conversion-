def temperature_convert():
  Question = int(input("Do you want to convert from Centigrade to Farenheit (1) or Farenheit to Centigrade? (2) "))
  if Question == 1:
    return True
  elif Question == 2:
    return True 
  else:
    print("Please enter the number next to the option you want.")
    temperature_convert()
temperature_convert()
