import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from Undersight import app, db, bcrypt, mail
from forms import (RegistrationForm, LoginForm, UpdateAccountForm, CommentForm,
                             PostForm, RequestResetForm, ResetPasswordForm)
from models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = 'home')


@app.route("/find_local_politicians")
def find_local_politicians():
    return render_template('find_local_politicians.html', title = 'Find Local Politicians')


@app.route("/log_in")
def log_in():
    return render_template('log_in.html', title = 'Log In')


@app.route("/log_out")
def log_out():
    return render_template('log_out.html', title = 'Log Out')


@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html', title = 'Sign Up')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


if __name__ == '__main__':
    app.run(debug=True)
