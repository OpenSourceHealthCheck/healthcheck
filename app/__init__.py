from flask import Flask

app = Flask(__name__)
app.secret_key = 'r;giouwew;jkgnre;oifjew;bnw4r80uewgreo4nriuehfjweoifreo;jewoghe;orw'

from app import views

