from flask import render_template
from app import app
from github3 import login
import os


@app.route('/')
def index():
	gh = login(token=os.environ['GITHUB_API_TOKEN'])
	repo = gh.repository('robintw', 'Py6S')

	#return repo.readme().decoded

	return render_template("index.html")