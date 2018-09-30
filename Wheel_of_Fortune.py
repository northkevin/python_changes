import random
import time


def word_choice():
    """ Picks a word at random from the text file of potential word choices. """
    words = open('WheelOfFortune.txt', 'r')
    w = words.read()
    words.close()

    choices = w.split(', ')
    return random.choice(choices)


def blanks(w):
    """ Creates a list of blank spaces to representing each letter in word w. """
    blanks = ['_ '] * len(w)
    return blanks


def spin():
    """ Selects a value at random from the tuple dollars. """
    dollars = (-1, 0, 100, 200, 300, 400, 500, 600,700 , 800, 900)
    return random.choice(dollars)


def display_current_winnings(word, blanks, guesses, winnings, turns):
    """Updates the user with their total winnings and the letters they have gotten correct."""
    for (index, letter) in enumerate(word):
        if letter in guesses:
            blanks[index] = '{0} '.format(letter)
    print("Your total winnings are ${0} with {1} spin(s) to go\n"
          "Here's what you have right so far:\n\n"
          "{2}\n\n"
          "Let's spin again!\n".format(winnings, turns, ''.join(blanks)))


def wheel_of_fortune():
    """ Play Wheel of Fortune! """

    a = 0                               # Value for if the user guesses the word correctly.
    w = word_choice()
    b = blanks(w)
    turns = 5 + len(w)                  # How many turns the user gets.
    winnings = 0                        # Total number of winnings.
    guesses = []                        # List of all letters that have been guessed.
    vowels = ('a', 'e', 'i', 'o', 'u')

    print("Time to play some Wheel of Fortune!\n"
          "Your word today is:\n\n"
          "{0}\n".format(''.join(b)))
    print("Let's spin the wheel!\n")

    # Play the game until the user runs out of turns.
    while turns != 0 and '_ ' in b:
        s = spin()
        # If the user spins a 'bankrupt'
        if s == -1:
            print("Oh no! You went bankrupt!. Your total winnings is now back to zero.\n"
                  "Let's spin again.\n")
            winnings = 0
        # if the user spins a 'lose a turn'
        elif s == 0:
            turns -= 1
            print("That's no fun, you lost a turn. You have {0} left.\n"
                  "Let's spin again\n".format(turns))
        # If the user spins a dollar amount.
        elif s > 0:
            print("You landed on ${0}! It's time to guess a letter!\n"
                  "Or if you think you know the word, guess that!\n"
                  "Remember, vowels will cost you $250\n".format(s))
            guess = input("What do you think it could be?\n")
            # The user makes an attempt at guessing the word.
            if len(guess) > 1:
                # The user guesses the correct word
                if guess == w:
                    winnings += s
                    a += 1
                    # print("That's correct! The word was {0} You've won ${1}".format(w, winnings))
                    break
                # The user's attempt at guessing the word was wrong.
                else:
                    print("\nSorry that isn't correct. Try again!")
                    turns -= 1
            # The user guesses a letter they have already guessed.
            elif guess in guesses:
                print("\nYou've already guessed that! Now you lose a turn.")
                turns -= 1
            # The user guesses a vowel.
            elif guess in vowels:
                # The user doesn't have enough to buy a vowel.
                if winnings < 250:
                    print("\nSorry you don't have enough money to buy a vowel. You lose a turn")
                    turns -= 1
                # The user guesses a vowel that is in the word.
                elif winnings > 250 and guess in w:
                    print("\nThat's correct!")
                    turns -= 1
                    winnings -= 250
                    guesses.append(guess)

                else:
                    print("\nSorry, that's incorrect. Let's try again")
                    turns -= 1
                    winnings -= 250
                    guesses.append(guess)
            # Any other letter is guessed.
            else:
                # The user guesses a correct letter.
                if guess in w:
                    print("\nThat's correct!" )
                    winnings += s
                    turns -= 1
                    guesses.append(guess)
                # The user guessed wrong.
                else:
                    print("\nSorry, that's incorrect. Let's try again")
                    turns -= 1
                    guesses.append(guess)

            display_current_winnings(w, b, guesses, winnings, turns)


    # Outputs once the game is over

    # The user guessed the correct word.
    if a == 1:
        print("\nDING DING DING\n"
              "YOU'VE WON ${0}!\n"
              "Way to go!".format(winnings))
    # The user ran out of guesses.
    elif '_ ' in b:
        print("Looks like you ran out of guesses.\n"
              "The word was '{0}'\n"
              "Better luck next time!".format(w))
    # The user completed the word by guessing the final word.
    else:
        print("\nDING DING DING\n"
              "YOU'VE WON ${0}!\n"
              "Way to go!".format(winnings))


# Run the game
wheel_of_fortune()
