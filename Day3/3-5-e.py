print("Welcome to the Love Calculator!")
n1 = "brad pitt"  # input("What's your name\n")
n2 = "Jeniffer Aniston"  # input("What is their name? \n")

nam1 = n1 + n2
name1 = nam1.lower()

t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
true = t + r + u + e
l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")
love = l + o + v + e


score = int(str(true) + str(love))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
