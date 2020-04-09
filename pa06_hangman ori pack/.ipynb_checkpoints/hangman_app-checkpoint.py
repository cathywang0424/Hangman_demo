"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

import random
randomWords = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry blueberry blackberry peach lychee muskmelon".split()

def generate_random_word():
    """ read a list of words from a file and pick a random one to return """
    return random.choice(randomWords)

def play_hangman():
   """ this is the python script version of the game, change the part with word into: word = generate_random_word() """
   print("The hangman app is under construction. Try again later!")

if __name__ == '__main__':
    play_hangman()
