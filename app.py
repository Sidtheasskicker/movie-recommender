from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/index.html')
def afterlogin():
    return render_template("afterlogin.html")


@app.route('/af')
def afterindex():
    return render_template("afterindex.html")


@app.route('/movies', methods=['POST', 'GET'])
def movies():
    return render_template("movies.html")


@app.route('/happy')
def happy():
    return render_template("happy.html")


@app.route('/emo')
def emo():
    return render_template("emo.html")


@app.route('/thrill')
def thrill():
    return render_template("thrill.html")


@app.route('/conf')
def conf():
    return render_template("conf.html")


@app.route('/about')
def about():
    return render_template("about.html")
