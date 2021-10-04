from flask import Flask, request
from .twitter_functions import upsert_author
from data_model import DB

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:////Users/dillonconroy/Code/Lambda/DS/U3/Twitter'
DB.init_app(app)


@app.route('/')
def landing:
    DB.create_all()
    return 'Welcome to my twitter app!'

@app.route('/add_author')
def add_author():
    author_handle = request.args(['author_handle'])
    author = upsert_author(author_handle = author_handle)
    return ', '.join([t.body for t in author.tweets])


app.run()

