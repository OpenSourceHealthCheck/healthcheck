from flask import render_template, request, Markup, redirect, url_for, flash
from app.healthcheck import healthcheck
from github3 import login
import os
import app.plugins

@healthcheck.route('/')
def index():
    return render_template("index.html")

@healthcheck.route('/run', methods=['POST', 'GET'])
def run_from_post():
    submitted_repo = request.form['repo']

    # if 'http' in submitted_repo:
    #   # We've got a full Github URL
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

        print(username, reponame)
    except:
        return "Error - Repo doesn't exist!"
    
    return redirect(url_for('run_from_url', username=username, reponame=reponame))
    #return run_from_url(username, reponame)

@healthcheck.route('/<username>/<reponame>')
def run_from_url(username, reponame):
    gh = login(token=os.environ['GITHUB_API_TOKEN'])

    repo = gh.repository(username, reponame)
    if repo is None:
        return "Error - Repo doesn't exist!"

    actives = app.plugins.load()
    results = [active.get_html(repo) for active in actives]
    passes = [active.get_passes() for active in actives]

    results = map(Markup, results)
    results = zip(results, passes)
    return render_template("results.html", name=repo.name, results=results)

@healthcheck.route('/create_issue', methods=["POST"])
def create_issue():
    gh = login(token=os.environ['GITHUB_API_TOKEN'])

    gh.create_issue(request.form['user'], request.form['repo'], request.form['title'], body=request.form['body'])

    flash("Added issue")
    return redirect(url_for('run_from_url', username=request.form['user'], reponame=request.form['repo']))
