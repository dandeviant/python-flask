#!/usr/bin/env python3

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # declare Flask object from flask library

@app.route('/') #Python decorator
@app.route('/<name>') #Python decorator with variable

def home(name=None):
	# Front page of Flask
	return render_template('home.html', name=name)

if __name__ == '__main__':
	app.run(debug=True)
