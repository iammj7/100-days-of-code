from art import logo, vs
from game_data import data
import random
# how to store the score
# how to compare a,b
# how to pick a,b for comparison like should be use random.choicr
score = 0

print(len(data))


def compare(a, b):
  """ This will compare A , B and return score"""
  if a > b:
    global score
    score += 1
    return score


def vs(game):
  choose = random.choice(data)

