import random

# Step 1: List of 5 predefined words
word_list = ["apple", "grape", "mango", "peach", "melon"]

# Step 2: Randomly choose a word
word = random.choice(word_list)

# Step 3: Create a list to store guessed letters (start with "_")
guessed = ["_"] * len(word)

# Step 4: Set the number of allowed wrong guesses
max_wrong_guesses = 6
wrong_guesses = 0

# Step 5: Create a list to store letters already guessed
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word: " + " ".join(guessed))

# Step 6: Main game loop
while wrong_guesses < max_wrong_guesses and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        # Reveal the correct letter in all positions
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct! " + " ".join(guessed))
    else:
        wrong_guesses += 1
        print(f"Wrong! You have {max_wrong_guesses - wrong_guesses} guesses left.")
        print("Current word: " + " ".join(guessed))

# Step 7: Check win or lose
if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("Sorry, you lost! The word was:", word)
