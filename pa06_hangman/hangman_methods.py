"""
   hangman_methods.py is used as a module in the hangman_webapp flask app
"""

import random
words = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry blueberry blackberry peach lychee muskmelon".split()

def generate_random_word():
    return random.choice(words)

def get_word_so_far(word):
    word_so_far = '-' * len(word)
    return word_so_far

def play_hangman():
    
    want_to_play = input("Do you want to play the game? Please enter y or n.")

    while want_to_play == "y":
        word= generate_random_word()
        guessed_letters = []
        guesses_left = 6
        letter = input("Enter a letter:")
        length = len(word)

        done = False
        while not done:
            if len(letter)>=2 or len(letter) == 0:
                guesses_left = guesses_left - 1
                print("Please enter one letter at a time")
                print("These are the letters you have guessed: ", guessed_letters)
                print("you have", guesses_left, "guesses left.")

            elif letter in guessed_letters:
                guesses_left = guesses_left - 1
                print("You already guessed that letter.")
                dashes = []
                for letter in word:
                    if letter in guessed_letters:
                        dashes += letter
                    else:
                        dashes += '-'
                print(dashes)
                print()
                print("These are the letters you have guessed: ", guessed_letters)
                print("you have", guesses_left, "guesses left.")

            elif letter not in word:
                guesses_left = guesses_left - 1
                guessed_letters.append(letter)
                print("The letter you guessed is not in the word.")
                dashes = []
                for letter in word:
                    if letter in guessed_letters:
                        dashes += letter
                    else:
                        dashes += '-'
                print(dashes)
                print()
                print("These are the letters you have guessed: ", guessed_letters)
                print("you have", guesses_left, "guesses left.")

            else:
                guessed_letters.append(letter)
                length = length-1
                dashes = []
                for letter in word:
                    if letter in guessed_letters:
                        dashes += letter
                    else:
                        dashes += '-'
                print(dashes)
                print()
                print("The letter you guessed is in the word.")
                print("These are the letters you have guessed: ", guessed_letters)
                print("you have", guesses_left, "guesses left.")

            if guesses_left == 0:
                done = True
                print("You lost, the word is ", word)
                want_to_play=input("Do you want to play another round? Please enter y or n.")
                if want_to_play=="y":
                    want_to_play=True
                if want_to_play=="n":
                    want_to_play=False
                    
            elif length == 0:
                done = True
                print("You won the game! The word is ", word)
  
            else:
                letter = input("Please guess a letter: ")



if __name__ == '__main__':
    play_hangman()


