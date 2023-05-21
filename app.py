from flask import Flask, render_template, url_for, redirect, session, request, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
db = SQLAlchemy(app)

class Login(db.Model):
     id = db.Column('id', db.Integer, primary_key=True)
     name = db.Column('name', db.String(30))
     last_name = db.Column('last_name', db.String(40))
     age = db.Column('age', db.Integer)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form["name"]
        last_name = request.form["last_name"]
        age = request.form["age"]
        login = Login(name=name, last_name=last_name, age=age)
        db.session.add(login)
        db.session.commit()
        flash("Added Successfully! ")
        return redirect(url_for("hellp world"))
    return render_template("login.html")
class Books(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(30))
    author = db.Column('author', db.String(40))
    price = db.Column('price', db.Integer)
@app.route("/books", methods=['GET', 'POST'])
def Books():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        price = request.form["price"]
        book = Books(title=title, author=author, price=price)
        db.session.add(book)
        db.session.commit()
        flash("Added Successfully! ")
        return redirect(url_for("hello_world"))
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


if __name__ == '__main__':
    app.run()