# this one has 3 menus small , medium , large upon choosing
#
print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is ${bill}.")

if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is ${bill}.")

if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is ${bill}.")
# menu has 3 items  so create 2 if and 1 else
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
