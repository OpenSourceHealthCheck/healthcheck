from app import app

from github3 import login


@app.route('/')
def index():
	gh = login(token='9829d6638caa5fc1ad576e4e345ca266fd626d8c')
	repo = gh.repository('robintw', 'Py6S')

	return repo.readme().decoded