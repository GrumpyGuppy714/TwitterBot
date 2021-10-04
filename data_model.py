from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Author(DB.Model):

    id = DB.column(DB.BigInteger, primary_key=True, nullable=False)
    name = DB.column(DB.String, nullable=False)


class Tweet(DB.Model):

    id = DB.column(DB.BigInteger, primary_key=True, nullable=False)
    body = DB.column(DB.Unicode(300), nullable=False)
    author_id = DB.column(DB.BigInteger, DB.ForeignKey('author.id'), nullable=False)
    author = DB.relationship('Author', backref=DB.backref('tweets', lazy=True))