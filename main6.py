#question three.
temp_value = float(input("Enter value of temperature in celcius: "))
if temp_value < -273.15:
  print("The temperature value is invalid because it is below absolute zerosolute zero")         

elif temp_value == -273.15:
  print("The temperature is absolute 0")
elif temp_value > -273 and temp_value < 0:
  print("The temperature is below freezing point.")
elif temp_value == 0:
  print("The temperature is at freezing point.")
elif temp_value > 0 and temp_value < 100:
  print("The temperature is in the normal range.")
elif temp_value == 100:
  print("The temperature is at the boiling point.")
else:
  print("The temperature is above boiling point. ")

