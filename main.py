#question four- An simple application to detect what grade a student is in.
credit = int(input("How many credits have you taken? "))
if credit <= 23:
  print("The student is a fresh man.")
elif credit > 23 and credit < 54:
  print("They are a sophomore.")
elif credit >= 54 and credit <=  83:
  print("They are juniors.")
else:
  print("They are seniors.")
