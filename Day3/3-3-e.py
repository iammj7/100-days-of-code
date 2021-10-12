year = int(input("Enter year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
# if year dividable by 4 and 100 and 400 leap year
# if year dividable by 4 and not 100 leap year
