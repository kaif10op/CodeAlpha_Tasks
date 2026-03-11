import random

words = ["python", "apple", "tiger", "chair", "river"]

word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

display_word = ["_"] * len(word)

print("Welcome to Hangman Game")

while incorrect_guesses < max_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess")
        print("Remaining attempts:", max_guesses - incorrect_guesses)

if "_" not in display_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)
