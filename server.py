from flask import Flask, redirect, render_template, session, request, jsonify
from random import randrange
from datetime import datetime as dt 

app = Flask(__name__)

secretKey = open('secret-key.txt', 'r').read().strip()
app.secret_key = secretKey

def initialize():
	session['gold'] = 0
	session['activities'] = []

def get_msg(gold, place, ts):
	ts_fmt = ts.strftime('%Y/%m/%d %I:%M:%S %p')
	if gold >= 0:
		return 'Earned {} gold from the {}! ({})'.format(gold, place, ts_fmt)
	else:
		return 'Entered the {} and lost {} gold.. Ouch.. ({})'.format(place, gold, ts_fmt)


@app.route('/')
def index():
	try:
		gold = session['gold']
	except:
		initialize()
		gold = session['gold']

	return render_template('index.html', 
		gold = gold)

@app.route('/process_money', methods=['POST'])
def process_money():
	ts = dt.now()
	place = request.form['place']
	
	if place == 'Farm':
		addgold = randrange(10, 20)
	elif place == 'Cave':
		addgold = randrange(5, 10)
	elif place == 'House':
		addgold = randrange(2, 5)
	elif place == 'Casino':
		addgold = randrange(-50, 50)

	
	msg = get_msg(addgold, place, ts)
	session['activities'].append(msg)

	newgold = session['gold'] + addgold # allow negative gold?
	session['gold'] = newgold
	
	return jsonify({
		'activities': session['activities'],
		'gold': session['gold'],
		'lastmsg': msg
		})
	
	# return redirect('/')

@app.route('/get_activities')
def get_activities():
	return jsonify({'activities': session['activities']})


@app.route('/reset')
def reset():
	initialize()
	return redirect('/')
	
app.run(debug=True)