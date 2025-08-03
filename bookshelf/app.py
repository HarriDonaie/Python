from datetime import date
from models import Book, Base, Author
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the SQLite database
engine = create_engine("sqlite:///bookshelf//books.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

# Create a new book
# new_book = Book(
#     title = "The Hobbit",
#     author = "J.R.R Tolkien",
#     genre = "Fantasy",
#     status = "Completed",
#     rating = 5,
#     review = "Loved the adventure and world-building",
#     date_added = date.today()
# )

# new_book = Book(
#     title = "The Devils",
#     author = "Joe Abercrombie",
#     genre = "Fantasy",
#     status = "Completed",
#     rating = 5,
#     review = "Suicide Squad set in historic Europe. Dope.",
#     date_added = date.today()
# )

# Add and commit to DB
session.add(new_book)
session.commit()

# Query all books
books = session.query(Book).all()
for book in books:
    print(f"{book.title} by {book.author} - {book.status}")