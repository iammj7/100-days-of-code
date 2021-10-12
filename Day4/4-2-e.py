import random

#  Printing and string asking for names
names_string = input("Give me everybody's names, seperated by a comma. ")
#  This will take all names and splits the name by comma $ stored as a list
names = names_string.split(",")
#  Get the total number of items in left.
randomm = len(names)
#  Generate random number between 0 and the last index.
random_ = random.randint(0, randomm - 1)
#  Printing name from the list with randomly generated number
print(names[random_] + " is going to buy the meal today!")

#  this is more easier way to pick random value.
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the milk today!")
