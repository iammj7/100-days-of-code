print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets $5.")
    elif age > 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    elif age >= 45 and age <= 55:
        print("Everythn gonna be alright. Have a free ride.")
    else:
        print("Adult tickets are $12.")
        bill = 12
    photos = input("Do you want a photo taken? Y or N. ")
    if photos == "Y":
        bill += 3
        print(f"Your final bill is {bill}")
    else:
        print(f"your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
