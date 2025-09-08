from flask import Flask, render_template, redirect, url_for, flash, request
from forms import LoginForm, RegisterForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin

app = Flask(__name__)
app.config.from_object('config.Config')

login_manager = LoginManager(app)
login_manager.login_view = "login"

# Dummy User class for login management without database
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    # Since no database, just return a generic User to allow login-required routes to work.
    # You can enhance this to manage actual user sessions or file-based users.
    return User(user_id)

@app.route('/')
def index():
    # Static sample books for display without database
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 299.99, "image": "book_placeholder.png"},
        {"title": "1984", "author": "George Orwell", "price": 199.99, "image": "book_placeholder.png"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 249.50, "image": "book_placeholder.png"},
        # add more books here as dictionaries
    ]
    return render_template("index.html", books=books)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Stub login: approve any email/password for demo (not secure, replace with real auth)
        user = User(id=form.email.data)
        login_user(user)
        flash("Logged in successfully.")
        return redirect(url_for('index'))
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for('index'))

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash("Registration functionality requires a user system which is not implemented.")
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route('/books')
def books():
    books = []  # No DB
    return render_template("book_list.html", books=books)

@app.route('/cart')
@login_required
def cart():
    items = []  # No DB
    return render_template("cart.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)
