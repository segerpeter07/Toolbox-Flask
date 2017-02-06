"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/hello/', methods=['GET', 'POST'])
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['GET'])
def login():
    if 'GET':
        return render_template('login.html')
    else:
        return render_template('hello.html')


@app.route('/profile', methods=['POST'])
def profile():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    if len(firstname) != 0 and len(lastname) != 0:
        return render_template('profile.html')
    else:
        return render_template('redirect.html')


if __name__ == '__main__':
    app.run()
