"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
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
	state['word']=hangman_app.generate_random_word()
	state['guesses'] = []
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()
	elif request.method == 'POST':
		letter = request.form['guess']
	if 'guess' in 'guesses':
		'guesses'.append('guess')
		print("You already guessed that letter. Please guess again.")
	elif 'guess' in 'word':
		print("The letter is in word!")
		'guesses'.append('guess')
		if 'word' == 'word_so_far':
			print("Contratulation!The word is:", 'word')
	elif 'guess' not in 'word':
		print("The letter is not in word. Please try again")

		# check if letter has already been guessed
        # and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them
		state['guesses'] += [letter]
		return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
