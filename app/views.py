from flask import render_template, request, Markup, redirect, url_for
from app import app
from github3 import login
import os
import plugins

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/run', methods=['POST', 'GET'])
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

        print username, reponame
    except:
        return "Error - Repo doesn't exist!"
    
    return redirect(url_for('run_from_url', username=username, reponame=reponame))
    #return run_from_url(username, reponame)

@app.route('/<username>/<reponame>')
def run_from_url(username, reponame):
    gh = login(token=os.environ['GITHUB_API_TOKEN'])

    repo = gh.repository(username, reponame)
    if repo is None:
        return "Error - Repo doesn't exist!"

    results = []
    actives = plugins.load()
    results.extend(active.get_html(repo) for active in actives)
    passes = []
    passes.extend(active.get_passes() for active in actives)
    print(actives)
    print(len(actives))

    results = map(Markup, results)
    results = zip(results, passes)
    return render_template("results.html", name=repo.name, results=results)

@app.route('/create_issue', methods=["POST"])
def create_issue():
    gh = login(token=os.environ['GITHUB_API_TOKEN'])

    gh.create_issue(request.form['user'], request.form['repo'], 'Add a README', body="Please add a README file to your repository.\nThis really helps to improve the sustainability of your software, and helps others pick up your code and get running with it easily.\n\n(This issue was created by the Open Source Health Checker tool at www.healthchecker.io)")

    return redirect(url_for('run_from_url', username=request.form['user'], reponame=request.form['repo']))