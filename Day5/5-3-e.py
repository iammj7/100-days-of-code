# empty var for stored range of number
total = 0
# Generating range of even numbers and assigning/addition them one by one to empty var
for i in range(0, 101, 2):
    total += i
print(total)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number

print(total2)
