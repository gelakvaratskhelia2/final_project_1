from flask import Flask, render_template, url_for, redirect, session, request, flash, get_flashed_messages, request
import requests
from bs4 import BeautifulSoup
import time
# import csv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(120), nullable=False)

    with app.app_context():

        db.create_all()

@app.route('/')
def home():
    url = 'http://books.toscrape.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        print(title, price)
        time.sleep(2)
    return render_template('index.html', books=books)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form["username"]
        flash("login succesfully")
        return redirect(url_for("/"))
    return render_template('login.html')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    with app.app_context():

        db.create_all()

@app.route("/books", methods=['GET', 'POST'])
def books():
    if request.method == "POST":
        title = request.form["title"]
        price = request.form["price"]
        book = books(title=title, price=price)
        db.session.add(book)
        db.session.commit()
        flash("Added Successfully! ")
        return redirect(url_for("Books"))
    return render_template("books.html")

@app.route ("/logout")
def logout():
    session.pop("username", None)
    return "You have been logged out. Goodbye!"
logout()

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == 'POST':
        return redirect(url_for('search_results'))
    return render_template('search.html')

@app.route('/Registration',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('register'))
    return render_template('registration.html')


if __name__ == '__main__':
    app.run()
