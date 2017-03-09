#!/usr/bin/env python
# coding=utf-8
 
"""
guess_num.py
L33T G4M3 M8.
"""

from argparse import ArgumentParser
from random import randint 
from sys import version_info

LANGUAGES = {
    "en_GB": {
        "guess_prompt_with_lives": "Guess the number between {lower_bound} and {upper_bound}. You have {guesses} guesses left: ",
        "guess_outwith_bounds": "Your guess was not within possible bounds. Enter a sensible guess: ",
        "guess_response_success": "You guessed right! You used {} guesses!",
        "game_fail": "You have failed. You have used all of your {guesses} guesses. The number was {number}.",
        "hint": " Number is {}.",
        "lower": "lower",
        "higher": "higher",
        "guess_response_fail": "Wrong.{hint} You have {guesses} guesses left. Try again: ",
        "replay_prompt": "Would you like to play again? (y/n): ",
        "gratitude_message": "Thanks for playing!",
        "wrong_key_prompt": "Input (y/n) please: "
    },
    "fr_FR": {
        "guess_prompt_with_lives": "Devinez le nombre entre {lower_bound} et {upper_bound}. Vous avez {guesses} devinez: ",
        "guess_outwith_bounds": "Votre conjecture était dans des limites possibles. Entrez une estimation sensible: ",
        "guess_response_success": "Vous avez deviné juste! Vous avez utilisé {} conjectures!",
        "game_fail": "Tu as échoué. Vous avez utilisé toutes vos {guesses} conjectures. Le nombre était {number}.",
        "hint": " Nombre est {}.",
        "lower": "inférieur",
        "higher": "plus élevé",
        "guess_response_fail": "Faux.{hint} Vous avez {guesses} crédits à gauche. Réessayer: ",
        "replay_prompt": "Voulez-vous jouer de nouveau? (y/n): ",
        "gratitude_message": "Merci d'avoir joué!",
        "wrong_key_prompt": "Entrée (y/n) s'il vous plaît: "
    }
}


def check_guess(message, lower_bound, upper_bound):
    """
    Checks whether the guess input by the user lies within the bounds of possible correct answers and asks for a new guess if this is not the case. 
    """
    guess = int(input(message))
    
    while guess < lower_bound or guess > upper_bound:
        guess = int(input(L["guess_outwith_bounds"]))
    
    return guess


def play_round(difficult=False, lives=5, lower_bound=0, upper_bound=20):
    """
    Play a single round of the number guessing game.
    """
    total_lives = lives
    random_number = randint(lower_bound, upper_bound)

    guess = check_guess(L["guess_prompt_with_lives"].format(lower_bound=lower_bound, upper_bound=upper_bound, guesses=lives), lower_bound, upper_bound)

    while True:
        if guess == random_number:
            print(L["guess_response_success"].format(total_lives + 1 - lives))
            break
    
        lives -= 1

        if not lives:
            print(L["game_fail"].format(guesses=total_lives, number=random_number))
            break
        
        hint = "" if difficult else L["hint"].format(
            L["lower"] if guess > random_number else L["higher"])

        guess = check_guess(L["guess_response_fail"].format(hint=hint, guesses=lives), lower_bound, upper_bound)


def input_character(prompt):
    """
    Allows support for Python versions 2 and 3.
    """
    if python_version == 3:
        return str(input(prompt))
    elif python_version == 2:
        return raw_input(prompt)
    else:
        exit("Only supports Python versions 2 and 3.")


def prompt_yn(prompt):
    """
    Allow user to input whether they want to continue playing. 
    """
    char_yn = input_character(prompt)
    
    while True:
        if char_yn == 'n':
            return False
        elif char_yn == 'y':
            print("")
            return True
        else:
            char_yn = input_character(L["wrong_key_prompt"])


def play_game(difficult=False, lives=5, lower_bound=0, upper_bound=20):
    """
    Play a single round of the number guessing game.
    """
    while True:
        play_round(difficult, lives, lower_bound, upper_bound)

        if not prompt_yn(L["replay_prompt"]):
            print(L["gratitude_message"])
            break 


def main():
    """
    Parses arguments from command line to play_game function.
    """
    global L
    global python_version

    python_version = version_info.major

    parser = ArgumentParser()

    parser.add_argument("-d", "--difficult", help="Set game mode to difficult.", 
        action="store_true")
    parser.add_argument("-l", "--lives", help="Set number of lives to play with.", type=int, 
        default=5)
    parser.add_argument("-lb", "--upper-bound", 
        help="Set the upper bound of the random integer number generator.", type=int, default=20)
    parser.add_argument("-ub", "--lower-bound", 
        help="Set the lower bound of the random integer number generator.", type=int, default=0)
    parser.add_argument("-i", "--language", help="Set the program language.", type=str, 
        default="en_GB")

    args = parser.parse_args()
    
    L = LANGUAGES[args.language]

    play_game(args.difficult, args.lives, args.lower_bound, args.upper_bound)


if __name__ == "__main__":
    main()
