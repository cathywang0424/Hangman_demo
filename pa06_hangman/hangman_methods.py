"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

def get_word_so_far(word):
    word_so_far = '-' * len(word)
    return word_so_far

if __name__ == '__main__':
    play_hangman()
