from Undersight import db
from flask_login import UserMixin

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique key for user
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

class User(db.Model):
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


'''
import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))


def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()


def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts
'''