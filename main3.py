#question two
temp_value = float(input("Enter temperature value: "))
unit = input("Enter unit of temperature f/c: ").lower()
if unit == "f":
  celcius = round(5/9 * (temp_value - 32),3)
  print(f"The temperature value from {temp_value} {unit} is {celcius} celcius")
elif unit == "c":
  fahrenheit = round(9/5 * (temp_value + 32),3)
  print(f"The temperature value from {temp_value} {unit} is {fahrenheit} fahrenheit")
else:
  print("omo...me I no sabi watin you enter o!")