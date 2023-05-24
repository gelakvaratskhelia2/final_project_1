from flask import Flask, render_template, url_for, redirect, session, request, flash, get_flashed_messages
import requests
from bs4 import BeautifulSoup
import time
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlte:///books.sqlite'
# app.config['SECRET_KEY'] = 'Python'
# db = SQLAlchemy(app)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form["username"]
        return redirect(url_for("hello my new user"))
    return render_template('login.html')
# class Books(db.Model):
#     id = db.Column('id', db.Integer, primary_key=True)
#     title = db.Column('title', db.String(30))
#     author = db.Column('author', db.String(40)) es wasashlelia
#     price = db.Column('price', db.Integer)

url = f"https://books.toscrape.com/catalogue/page-1.html"
r = requests.get(url)
print(r.status_code)
content = r.text
soup = BeautifulSoup(content,'html.parser')
body = soup.find("body")
wrapper = body.find("div",{'class':'container-fluid page'})
pg_inner = wrapper.find('div',{'class':'page_inner'})
row_1 = pg_inner.find('div',{'class':'row'})
column = row_1.find('div',{'class':'col-sm-8 col-md-9'})
section = column.find("section")
div = section.find("div")
row_2 = section.find("ol")
col = section.find("li")
article=col.find("article")
all_books = section.find_all('li')
r = requests.get(url)
print(r.status_code)
content = r.text
soup = BeautifulSoup(content,'html.parser')
body = soup.find("body")
wrapper = body.find("div",{'class':'container-fluid page'})
pg_inner = wrapper.find('div',{'class':'page_inner'})
row_1 = pg_inner.find('div',{'class':'row'})
column = row_1.find('div',{'class':'col-sm-8 col-md-9'})
section = column.find("section")
div = section.find("div")
row_2 = section.find("ol")
col = section.find("li")
article=col.find("article")
all_books = section.find_all('li')

for container in all_books:
            book_title = container.find('h3')
            book_price = container.find('div',{'class':'product_price'})
            title = book_title.a.text
            price = book_price.p.text
            print(title, price)
            time.sleep(1)



@app.route("/books", methods=['GET', 'POST'])
def Books():
    if request.method == "POST":
        title = request.form["title"]
        # author = request.form["author"]
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

@app.route('/Registration',methods=['GET','POST'])
def Register():
    if request == 'post':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        registration = Register(firstname=firstname,lastname=lastname,username=username,email=email,password=password)
        # db.session.add(registration)
        # db.session.commit()
        flash('Registration was successful')
        return redirect(url_for('register'))
    return render_template('registration.html')


if __name__ == '__main__':
    app.run()