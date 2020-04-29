"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""


import random

def generate_random_word():
    words = "apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry blueberry blackberry peach lychee muskmelon".split()
    return random.choice(words)
#to co-respond to the webpage - attribute the lines to the webpage
def word_check(state):
    current = []
    for g in state['word']:
        if g in state['guessed_letters']:
            current.append(g)
        else:
            current.append(" _ ")
    current = "".join(current)
    return current

def check(word, guessed_letters, guess):
    blank = ""
    bingo = 0
    for i in word:
        if i in guessed_letters:
            blank = blank + i
        else:
            blank = blank + '_ '
        if i == guess:
            bingo = bingo + 1
    if bingo >= 1:
        print("Great! The letter is in the word.")
        return blank, True # return to bingo ==True means gussed a correct letter

    else:
        print("Sorry,the letter is not in the word.")
        return blank, False  # return to bingo else means gussed a wrong letter and guesses_left - 1


def play_hangman():
    want_to_play=input("Do you want to play the game? Please enter y or n.")
    if want_to_play=="y":
        want_to_play=True
        print("Welcome to Hangman! The word you will be guessing is a fruit.")
    if want_to_play=="n":
        want_to_play=False
    while(want_to_play):
        word = generate_random_word()
        #word = "apple"
        guessed_letters = []
        guesses_left = 6
        guess = input("Enter a letter:")
        done = False
        while not done:
            if guess in guessed_letters:
                guessed_letters.append(guess)
                print("You already guessed that letter.")
                guess = input("Enter a letter:")

            elif len(guess) == 1:
                guessed_letters.append(guess)
                result, bingo = check(word, guessed_letters, guess)

                # Guessed correct word finally
                if result == word:
                    done = True
                    print("Contratulation!The word is:", word)
                    want_to_play=input("Do you want to play another round? Please enter y or n.")
                    if want_to_play=="y":
                        want_to_play=True
                    if want_to_play=="n":
                        want_to_play=False

                # if guessed correct letter, keep the guesses_left
                elif bingo == True:
                    print(result)
                    print("You have", guesses_left, "guesses left.")
                    guess = input("Enter a letter:")

                # if  guessed wrong letter, -1
                else:
                    print(result)
                    guesses_left = guesses_left - 1
                    print("You have", guesses_left, "guesses left.")
                    guess = input("Enter a letter:")
                    if guesses_left == 0:
                        print("Sorry, you used up all chances to guess, you lose the game.")
                        print("The word is", word, '\n')
                        want_to_play=input("Do you want to play the game? Please enter y or n.")
                        if want_to_play=="y":
                            want_to_play=True
                            print("Welcome to Hangman! The word you will be guessing is a fruit.")
                        if want_to_play=="n":
                            want_to_play=False
                        break
            else:
                print('Error input! Let us start over!') # If type in two letters mistakenly
                break


if __name__ == '__main__':
    play_hangman()
