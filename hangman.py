import random

play_again = "Y"
games_played = 0
games_won = 0
games_lost = 0

# List of words
categories = {
    "Programming": [
        "python",
        "coding",
        "github",
        "developer",
        "algorithm"
    ],

    "Fruits": [
        "apple",
        "banana",
        "orange",
        "grapes",
        "mango"
    ],

    "Technology": [
        "computer",
        "keyboard",
        "internet",
        "software",
        "database"
    ]
}
word_hints = {
    "PYTHON": "Popular programming language.",
    "CODING": "Writing computer programs.",
    "GITHUB": "Website to host code repositories.",
    "DEVELOPER": "A person who develops software.",
    "ALGORITHM": "Step-by-step solution to a problem.",

    "APPLE": "A red or green fruit.",
    "BANANA": "A long yellow fruit.",
    "ORANGE": "A citrus fruit.",
    "GRAPES": "Small fruits that grow in bunches.",
    "MANGO": "Known as the king of fruits.",

    "COMPUTER": "An electronic machine.",
    "KEYBOARD": "Used to type on a computer.",
    "INTERNET": "Worldwide network.",
    "SOFTWARE": "Programs that run on a computer.",
    "DATABASE": "Stores and manages data."
}

while play_again == "Y":
    games_played += 1

    # Select random category and word
    category = random.choice(list(categories.keys()))
    secret_word = random.choice(categories[category]).upper()

    guessed_letters = []
    wrong_letters = []

    # Difficulty
    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        attempts = 8
    elif choice == "2":
        attempts = 6
    elif choice == "3":
        attempts = 4
    else:
        print("Invalid choice! Medium selected.")
        attempts = 6

    print("\n" + "=" * 45)
    print("          HANGMAN GAME")
    print("=" * 45)
    print("Category:", category)
    print("Hint:", word_hints[secret_word])

    while attempts > 0:

        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong Letters:", " ".join(wrong_letters))

        # Win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations!")
            print("You guessed the word:", secret_word)
            games_won += 1
            break

        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct!")
        else:
            attempts -= 1
            wrong_letters.append(guess)
            print("❌ Wrong!")
            print("Attempts left:", attempts)

    else:
      print("\n💀 Game Over!")
      print("The word was:", secret_word)
      games_lost += 1
    if games_played > 0:
        win_percentage = (games_won / games_played) * 100
    else:
        win_percentage = 0

    print("\n" + "=" * 40)
    print("        SCORE")
    print("=" * 40)
    print("Games Played :", games_played)
    print("Games Won    :", games_won)
    print("Games Lost   :", games_lost)
    print(f"Win Percentage : {win_percentage:.2f}%")
    print("=" * 40)

    play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()
    if play_again != "Y":
        break  

print("\nThank you for playing!")