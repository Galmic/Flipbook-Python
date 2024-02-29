"""
This module implements a simple Flask application.
"""

from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pdf.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Item(db.Model):
    """Class representing a PDF"""

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=False)
    owner = db.Column(db.String(length=30), nullable=False)
    created = db.Column(db.Date, default=datetime.now)

    def __repr__(self):
        return f"Item {self.name}"


# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
@app.route("/home")
def home_page():
    """Function to home page"""
    return render_template("home.html")


@app.route("/collections")
def collections_page():
    """Function to Collection page"""

    items = Item.query.all()

    return render_template("collections.html", items=items)


@app.route("/login")
def login_page():
    """Function to Login page"""
    return render_template("login.html")


@app.route("/register")
def register_page():
    """Function to Register page"""
    return render_template("register.html")


@app.route("/pdf/<book_id>")
def books_collection(book_id):
    """Function dynamic webpages."""
    return f"<h1>Ths will show the flipbook ID {book_id}</h1>"


if __name__ == "__main__":
    app.run(debug=True)


# End-of-file (EOF)
