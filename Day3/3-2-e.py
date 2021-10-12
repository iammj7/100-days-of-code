height = float(input("Enter your height in cm? "))
weight = int(input("Enter you weight in kg? "))

#  round the result value
bmi = round(weight / (height ** 2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}, You have normal weight.")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, You are over weight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, You are obesse.")
else:
    print("You are clinically obesse")
