from app import app
from models import db, Book

# Initialize db with the app
db.init_app(app)

with app.app_context():
    db.create_all()
    
    sample_books = [
        Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price=299.99, image="book_placeholder.png"),
        Book(title="1984", author="George Orwell", price=199.99, image="book_placeholder.png"),
        Book(title="To Kill a Mockingbird", author="Harper Lee", price=249.50, image="book_placeholder.png"),
        Book(title="Pride and Prejudice", author="Jane Austen", price=349.00, image="book_placeholder.png"),
        Book(title="Moby-Dick", author="Herman Melville", price=399.99, image="book_placeholder.png"),
        Book(title="War and Peace", author="Leo Tolstoy", price=499.99, image="book_placeholder.png"),
        Book(title="The Catcher in the Rye", author="J.D. Salinger", price=279.99, image="book_placeholder.png"),
        Book(title="The Hobbit", author="J.R.R. Tolkien", price=329.99, image="book_placeholder.png"),
        Book(title="Fahrenheit 451", author="Ray Bradbury", price=219.99, image="book_placeholder.png"),
        Book(title="Brave New World", author="Aldous Huxley", price=289.99, image="book_placeholder.png"),
        Book(title="Jane Eyre", author="Charlotte Brontë", price=259.99, image="book_placeholder.png"),
        Book(title="Animal Farm", author="George Orwell", price=189.99, image="book_placeholder.png"),
        Book(title="Crime and Punishment", author="Fyodor Dostoevsky", price=379.99, image="book_placeholder.png"),
        Book(title="The Odyssey", author="Homer", price=459.99, image="book_placeholder.png"),
        Book(title="The Divine Comedy", author="Dante Alighieri", price=439.99, image="book_placeholder.png")
    ]

    db.session.add_all(sample_books)
    db.session.commit()

    print(f"Database created and {len(sample_books)} sample books inserted successfully.")
