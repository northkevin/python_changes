import random
import time

BLANK_LETTER='_'


def word_choice():
    """ Picks a word at random from the text file of potential word choices. """
    words = open('WheelOfFortune.txt', 'r')
    w = words.read()
    words.close()

    choices = w.split(', ')
    return random.choice(choices)


def init_game_board(word):
    """ Creates a list of blank spaces to representing each letter in word w. """
    game_board = [BLANK_LETTER] * len(word)
    return game_board


def spin():
    """ Selects a value at random from the tuple dollars. """
    dollars = (-1, 0, 100, 200, 300, 400, 500, 600,700 , 800, 900)
    return random.choice(dollars)


def display_board_and_current_winnings(game_board, winnings, turns_remaining):
    """Updates the user with their total winnings and the letters they have gotten correct."""
    print("Your total winnings are ${0} with {1} spin(s) to go\n"
          "Here's what you have right so far:\n\n"
          "{2}\n\n"
          "Let's spin again!\n".format(winnings, turns_remaining, ' '.join(game_board)))


def get_number_of_remaining_turns(total_turns, current_turn):
    return total_turns - current_turn


# Lists are mutable.. the 'game_board' will be updated outside of this method.
def update_board(game_board, actual_word, choice):
    for pos, letter in enumerate(actual_word):
        if choice.lower() == letter.lower():
            game_board[pos] = choice.lower()


def is_game_board_complete(game_board):
    return BLANK_LETTER not in game_board


# from sets import Set

def wheel_of_fortune():
    """ Play Wheel of Fortune! """

    a = 0                               # Value for if the user guesses the word correctly.
    w = word_choice()
    game_board = init_game_board(w)
    total_turns = 5 + len(w)            # How many turns the user gets.
    winnings = 0                        # Total number of winnings.
    guesses = []                        # List of all letters that have been guessed.
    vowels = ('a', 'e', 'i', 'o', 'u')

    print("Time to play some Wheel of Fortune!\n"
          "Your word today is:\n\n"
          "{0}\n".format(' '.join(game_board)))
    print("Let's spin the wheel!\n")

    # Play the game until the user runs out of turns.
    for current_turn in range(total_turns):
        if is_game_board_complete(game_board): break
        s = spin()
        # If the user spins a 'bankrupt'
        if s == -1:
            print("Oh no! You went bankrupt!. Your total winnings is now back to zero.\n"
                  "Let's spin again.\n")
            winnings = 0
        # if the user spins a 'lose a turn'
        elif s == 0:
            print("That's no fun, you lost a turn. You have {0} left.\n"
                  "Let's spin again\n".format(get_number_of_remaining_turns(total_turns, current_turn)))
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
            # The user guesses a letter they have already guessed.
            elif guess in guesses:
                print("\nYou've already guessed that! Now you lose a turn.")
            # The user guesses a vowel.
            elif guess in vowels:
                # The user doesn't have enough to buy a vowel.
                if winnings < 250:
                    print("\nSorry you don't have enough money to buy a vowel. You lose a turn")
                # The user guesses a vowel that is in the word.
                elif winnings > 250 and guess in w:
                    print("\nThat's correct!")
                    winnings -= 250
                    guesses.append(guess)
                    update_board(game_board, w, guess)
                else:
                    print("\nSorry, that's incorrect. Let's try again")
                    winnings -= 250
                    guesses.append(guess)
            # Any other letter is guessed.
            else:
                # The user guesses a correct letter.
                if guess in w:
                    print("\nThat's correct!" )
                    winnings += s
                    guesses.append(guess)
                    update_board(game_board, w, guess)

                # The user guessed wrong.
                else:
                    print("\nSorry, that's incorrect. Let's try again")
                    guesses.append(guess)

            display_board_and_current_winnings(game_board, winnings, get_number_of_remaining_turns(total_turns, current_turn))


    # Outputs once the game is over

    # The user guessed the correct word.
    if a == 1:
        print("\nDING DING DING\n"
              "YOU'VE WON ${0}!\n"
              "Way to go!".format(winnings))
    # The user ran out of guesses.
    elif not is_game_board_complete(game_board):
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
