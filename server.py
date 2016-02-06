from flask import Flask, render_template, request, redirect, flash, session
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "snuh"
# This will have the name of the sql database
mysql = MySQLConnector('') 

@app.route('/')
def index():
	if session:
		session.pop('name');
	return render_template('index.html')

@app.route('/nameget', methods=['POST'])
def nameget():
	print request.form
	for item in request.form:
		session['name'] = item
	return render_template('partial.html')

@app.route('/success')
def success():
	return render_template('success.html');

app.run(debug=True)