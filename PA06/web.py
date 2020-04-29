"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import web_app
app = Flask(__name__)

global state
state = {'guessed_letters':[],
         'word':"interesting",
         'word_so_far':"-----------",
         'done':False}

@app.route('/')
@app.route('/main')
def main():
 return render_template('hangman.html')

@app.route('/start')
def play():
 global state
 state['word']=web_app.generate_random_word()
 state['guessed_letters'] = []
 word_so_far = web_app.word_check(state)
 state['word_so_far'] = word_so_far
 print(state)
 return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
    global state
    word_so_far = web_app.word_check(state)
    state['word_so_far'] = word_so_far
    if request.method == 'GET':
        return play()

    elif request.method == 'POST':
        guess = request.form['guess']
        guessed_letters = []
        guessed_letters.append(guess)
        guessed_letters= "".join(guessed_letters)
        word=state['word']

        already_guessed = False
        word_length = False
        win = False

        if len(guess) > 1:
            word_length = True
            print("Please enter only 1 letter at a time.")
        if guess in word:
            print("Great! The letter is in the word!")
        elif guess in state['guessed_letters']:
            already_guessed = True
            print("You already guessed that letter. Please guess another letter.")

        # then see if the word is complete
        state['guessed_letters'] += [guess]
        word_so_far = web_app.word_check(state)
        state['word_so_far']= word_so_far
        if state['word_so_far'] == state['word']:
            win = True
            print("Congratulation! You have the correct word!")
     # if letter not in word, then tell them
        elif guess not in word:
            print("Sorry, this letter is not in the word.")
        return render_template('play.html',state=state,guess=guess,guessed_letters=state['guessed_letters'],word=state['word'],word_length=word_length,already_guessed=already_guessed,win=win)
@app.route('/About')
def About():
    return render_template("About.html")

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
