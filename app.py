from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm, RegisterForm
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    UserMixin,
)

app = Flask(__name__)
app.config.from_object("config.Config")

login_manager = LoginManager(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    # Dummy user loader without a database
    return User(user_id)


@app.route("/")
def index():
    books = [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "price": 299.99,
            "image": "book_placeholder.png",
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "price": 199.99,
            "image": "book_placeholder.png",
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "price": 249.50,
            "image": "book_placeholder.png",
        },
        # Add more books here as dictionaries if needed
    ]
    return render_template("index.html", books=books)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(id=form.email.data)
        login_user(user)
        flash("Logged in successfully.")
        return redirect(url_for("index"))
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash("Registration requires a user system which is not implemented.")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/books")
def books():
    books = []  # No database, empty list
    return render_template("book_list.html", books=books)


@app.route("/cart")
@login_required
def cart():
    items = []  # No database, empty list
    return render_template("cart.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
