import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_game = False

print(logo)

print(f"The solution is {chosen_word}")

display = []
for i in range(word_length):
    display += "_"

while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, That's not in the word. You lose a")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")
    # Join all elements in display list and turn it into string
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You win.")
    print(stages[lives])
