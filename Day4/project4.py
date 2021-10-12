import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
maps = [rock, paper, scissors]

#  check
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalied number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("draw")
elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalied number, you lose!")
