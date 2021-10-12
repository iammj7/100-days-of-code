print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip_n = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

nbill = round(bill * (tip_n / 100) + bill, 2)
split = nbill / people

print(f"Each person should pay: ${split}")
