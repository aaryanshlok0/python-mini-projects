'''
Bagels - A Detective Logic Game

Description:
    Bagels is a number-guessing game where the computer generates a
    random 3-digit secret number with no repeated digits. The player
    must guess the secret number within a limited number of attempts.

Game Rules:
    • The secret number consists of exactly 3 unique digits.
    • After each valid guess, the player receives clues:
        - Fermi : A correct digit in the correct position.
        - Pico  : A correct digit in the wrong position.
        - Bagels: No correct digits.
    • Invalid guesses (wrong length, non-numeric characters, or
      repeated digits) are rejected and do not count as an attempt.
    • The game ends when the player guesses the secret number or
      exhausts all attempts.

Functions:
    get_secret_no()
        Generates and returns a random 3-digit secret number.

    user_guess(secret_code, guess)
        Compares the player's guess with the secret number and
        returns the appropriate clues.

    is_valid_guess(guess)
        Validates the player's input.

    main()
        Controls the overall game flow.

Author: Aaryan Shlok
Language: Python

'''


import random

print("Welcome to Bagels! A detective logic game")


characters=['0','1','2','3','4','5','6','7','8','9']


def get_secret_no():
    ''' Generate and return a random 3-digit secret number with unique digits.'''

    random.shuffle(characters)
    shuffled_list=characters[0:3]
    secret_code="".join(shuffled_list)
    return secret_code

def user_guess(secret_code,guess):
    '''
    Compare the player's guess with the secret number and
    return the clues (Fermi, Pico, or Bagels).
    
    '''

    clues=[]
    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            clues.append("Fermi")
        elif guess[i] in secret_code:
            clues.append('Pico')
    if len(clues)==0:
        return "Bagels!"
    
    return " ".join(clues)




def is_valid_guess(guess):
    '''
  
    Check whether the player's guess is valid.

    A valid guess:
    - Contains exactly 3 digits.
    - Contains only numeric characters.
    - Has no repeated digits.

    Returns:
        bool: True if the guess is valid, otherwise False.
    
    '''
    if len(guess)!=3:
        return False
    if not guess.isdigit():
        return False
    if len(guess)!=len(set(guess)):
        return False
    return True

def main():
    '''
    Run the Bagels game by generating a secret number,
    validating player input, tracking attempts,
    displaying clues, and determining the game's outcome. 
    '''

    MAX_ATTEMPT=10
    USER_ATTEMPT=1
    secret_code=get_secret_no()
    won=False

    while USER_ATTEMPT<=MAX_ATTEMPT:
        guess=input("Enter your guess: ")

        if is_valid_guess(guess)==False:
            print("Invalid Guess!")
            continue
        clue=user_guess(secret_code,guess)
        print(clue)

        if guess==secret_code:
            print("Congratulations!")
            won=True
            break
        print(f"No of attempts remaining: ",MAX_ATTEMPT-USER_ATTEMPT)
        USER_ATTEMPT+=1

    if won==False:
        print(f"Secret code: {secret_code}")


main()

