#!/usr/bin/env python3
"""Sample Flask"""

from flask import Flask 

app = Flask(__name__) # declare Flask object from flask library

@app.route('/') #Python decorator 

def index():
	# Front page of Flask
	return "Hello World"

if(__name__ == '__main__'):
	app.run()