# fizzBuzz

# Generating range of numbers
for i in range(1, 101):
    # Checking if number 3, and 5 is divisible
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Cheking if 3 is divisible
    elif i % 3 == 0:
        print("Fizz")
    # Checking if 5 is divisible
    elif i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
    # else printing the remaining numbers
    else:
        print(i)
