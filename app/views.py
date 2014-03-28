from flask import render_template, request, Markup
from app import app
from github3 import login
import os

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/run', methods=['POST', 'GET'])
def run():
	results = ['<div>Some result here</div>',
			   '<div>Another result here</div>']

	results = map(Markup, results)
	return render_template("results.html", results=results)