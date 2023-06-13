sign = ""
percentage = float(input("What is your overall course grade? "))

#grading statements
if percentage >= 90:
  letter = "A"

elif percentage >= 80:
  letter = "B"

elif percentage >= 70:
  letter = "C"

elif percentage >= 60:
  letter = "D"

else:
  letter = "F"

#plus or minus
if percentage >= 60 and percentage < 93:
  if percentage % 10 >= 7:
    sign = "+"
  elif percentage % 10 < 3:
    sign = "-"

    #print here
if percentage >= 70:
  print(f"\nGreat job! You got an {letter+sign}. You passed the class.")

elif percentage <= 70:
  print(
    f"\nYou did not pass the class. You got an {letter+sign}. Next time just work a little harder and you will pass."
  )