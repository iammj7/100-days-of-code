from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':

        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


answer = randint(1, 100)
print("Welcome to the number Guessing game!")
print("I'm thinking of a number between 1 to 100.")

turns = set_difficulty()

print(f"You have {turns} attemps remaining to guess the number.")

guess = int(input("Make a guess: \n"))

check_answer(guess, answer)
