# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random


def game():
    print(")---------------------------(")
    print("Welcome to Number Guessing Game")
    print(")---------------------------(")
    print("You see 3 difficulty levels")
    print("1. Easy - (1 - 10)")
    print("2. Normal - (1 - 100)")
    print("3. Hard - (1 - 1000) / Good luck!")
    print("4. Exit")
    try:
        level = int(input("Enter difficulty level: "))
        if level == 1:
            easy()
        elif level == 2:
            normal()
        elif level == 3:
            hard()
        elif level == 4:
            print("Thanks for playing")
            exit(0)
        else:
            print("Invalid input, must be a number (1, 2, 3)")
            game()
    except ValueError:
        print("Invalid input, must be a number (1, 2, 3)")
        game()


def easy():
    lives = 10
    number = random.randint(1, 10)
    print("")
    print("You have chosen the easy difficulty. Good luck!")
    print("")
    print("You have 10 attempts to guess the number (1-10)")
    print("")
    while lives > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess == number:
                print("")
                print(f"You guessed it, it was {number}")
                print("")
                game()
            elif guess > number:
                lives -= 1
                print("")
                print(f"Too high! You have {lives} attempts left")
                print("")
            elif guess < number:
                lives -= 1
                print("")
                print(f"Too low! You have {lives} attempts left")
                print("")
            if lives == 0:
                print("")
                print(f"You lost! The number was {number}")
                print("")
                game()
        except ValueError:
            print("Invalid input, must be a number")


def normal():
    lives = 7
    number = random.randint(1, 100)
    print("")
    print("You have chosen the normal difficulty. Good luck!")
    print("")
    while lives > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess == number:
                print("")
                print(f"You guessed it, it was {number}")
                print("")
                game()
            elif guess > number:
                lives -= 1
                print("")
                print(f"Too high! You have {lives} attempts left")
                print("")
            elif guess < number:
                lives -= 1
                print("")
                print(f"Too low! You have {lives} attempts left")
                print("")
            if lives == 0:
                print("")
                print(f"You lost! The number was {number}")
                print("")
                game()
        except ValueError:
            print("Invalid input, must be a number")


def hard():
    lives = 5
    number = random.randint(1, 1000)
    print("")
    print("You have chosen the hard difficulty. Good luck!")
    print("")

    while lives > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess == number:
                print("")
                print(f"You guessed it, it was {number}")
                print("")
                game()
            elif guess > number:
                lives -= 1
                print("")
                print(f"Too high! You have {lives} attempts left")
                print("")
            elif guess < number:
                lives -= 1
                print("")
                print(f"Too low! You have {lives} attempts left")
                print("")
            if lives == 0:
                print("")
                print(f"You lost! The number was {number}")
                print("")
                game()
        except ValueError:
            print("Invalid input, must be a number")


game()
