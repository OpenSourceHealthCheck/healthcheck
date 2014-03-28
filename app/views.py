from flask import render_template, request, Markup
from app import app
from github3 import login
import os

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/run', methods=['POST', 'GET'])
def run():
	gh = login(token=os.environ['GITHUB_API_TOKEN'])

	submitted_repo = request.form['repo']

	# if 'http' in submitted_repo:
	# 	# We've got a full Github URL
	try:
		if ".git" in submitted_repo:
			# We're dealing with a clone URL
			if "git@github.com" in submitted_repo:
				# SSH clone URL
				splitted = submitted_repo.split(':')[1].split('/')
				username = splitted[-2]
				reponame = splitted[-1]
			elif "https" in submitted_repo:
				# HTTPS URL
				splitted = submitted_repo.split('/')
				username = splitted[-2]
				reponame = splitted[-1]

			reponame = reponame.replace('.git', '')
		else:
			splitted = submitted_repo.split('/')
			username = splitted[-2]
			reponame = splitted[-1]

		print username, reponame
		repo = gh.repository(username, reponame)
		if repo is None:
			return "Error - Repo doesn't exist!"
	except:
		return "Error - Repo doesn't exist!"
	# else:




	results = ['<div><b>Repository:</b> %s</div>' % (repo.name),
			   '<div><b>Watchers:</b> %s</div>' % (repo.watchers)]

	results = map(Markup, results)
	return render_template("results.html", results=results)