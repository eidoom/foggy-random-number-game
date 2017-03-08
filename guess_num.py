"""
guess_num.py
L33T G4M3 M8.
"""

from argparse import ArgumentParser
from random import randint 

LANGUAGES = {
    "en_GB":{
        "guess_prompt_with_lives":"Guess the number between {lower_bound} and {upper_bound}. You have {guesses} guesses left: ",
        "guess_response_success":"You guessed right! You used {} guesses!",
        "game_fail":"You have failed. You have used all of your {guesses} guesses. The number was {number}.",
        "hint":" Number is {}.",
        "lower":"lower",
        "higher":"higher",
        "guess_response_fail":"Wrong.{hint} You have {guesses} guesses left. Try again: ",
        "replay_prompt":"Would you like to play again? (y/n): ",
        "gratitude_message":"Thanks for playing!",
        "wrong_key_prompt":"Input (y/n) please: "
    }
}

def play_round(difficult=False, lives=5, lower_bound=0, upper_bound=20):
    """
    Play a single round of the number guessing game.
    """
    total_lives = lives
    rand_num = randint(lower_bound, upper_bound)
    guess = int(input(L["guess_prompt_with_lives"].format(
        lower_bound=lower_bound, upper_bound=upper_bound, guesses=lives)))
    
    while True:
        if guess == rand_num:
            print(L["guess_response_success"].format(total_lives + 1 - lives))
            break
    
        lives -= 1

        if not lives:
            print(L["game_fail"].format(guesses=total_lives, number=rand_num))
            break
        
        hint = "" if difficult else L["hint"].format(
            L["lower"] if guess > rand_num else L["higher"])

        guess = int(input(L["guess_response_fail"].format(hint=hint, guesses=lives)))


def prompt_yn(prompt):
    """
    Allow user to input whether they want to continue playing. 
    """
    char_yn = raw_input(prompt)
    
    while True:
        if char_yn == 'n':
            return False
        elif char_yn == 'y':
            print("")
            return True
        else:
            char_yn = raw_input(L["wrong_key_prompt"])


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
    global L

    parser = ArgumentParser()

    parser.add_argument("-d", "--difficult", help="Set game mode to difficult.", 
        action="store_true")
    parser.add_argument("-l", "--lives", help="Set number of lives to play with.", type=int, 
        default=5)
    parser.add_argument("-lb", "--upper-bound", 
        help="Set the upper bound of the random integer number generator.", type=int, default=20)
    parser.add_argument("-ub", "--lower-bound", 
        help="Set the lower bound of the random integer number generator.",type=int, default=0)
    parser.add_argument("-i", "--language", help="Set the program language.", type=str, 
        default="en_GB")

    args = parser.parse_args()
    
    L = LANGUAGES[args.language]

    play_game(args.difficult, args.lives, args.lower_bound, args.upper_bound)


if __name__ == "__main__":
    main()
