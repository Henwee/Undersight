from flask import Flask, render_template, flash

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


if __name__ == '__main__':
    app.run(debug=True)
