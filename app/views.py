from flask import render_template
from app import app
from github3 import login
import os


@app.route('/')
def index():
	return render_template("index.html")