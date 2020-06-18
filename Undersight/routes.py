from flask import render_template, url_for, flash, redirect, abort, request
from Undersight.forms import PostForm, RegistrationForm
from Undersight.models import Post
from Undersight import app,db,bcrypt
#from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template('index.html',posts=posts)

@app.route('/post',methods = ['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('post.html', form= form)

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()