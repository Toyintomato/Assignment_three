# Question one
# this program accepts the length in cm and converts it to inches.ccepts the length in cm and converts it to inches.

len_cm = float(input("Enter length in cm: "))
len_inch = round((len_cm / 2.54),3)
if len_cm < 0:
  print("Invalid Entry")
else:
  print(f"The length in inches is {len_inch}")