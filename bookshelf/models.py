from sqlalchemy import Column, Integer, String, Date, Text, create_engine, ForeignKey, Table, Double, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Association table for the many-to-many relationship
book_authors = Table(
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("author_id", ForeignKey("authors.id"), primary_key=True)
)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True)
    title = Column(String, nullable=False)
    genre = Column(String)
    status = Column(String)  # e.g. To Read, Reading, Completed
    rating = Column(Integer)
    review = Column(Text)
    date_added = Column(Date)
    publisher = Column(String)
    publication_date = Column(Date)
    isbn = Column(String)
    language = Column(String)
    genre = Column(String)
    series = Column(String)
    series_number = Column(Double) #consider additional series table
    format = Column(String)
    page_count = Column(Integer)
    condition = Column(String)
    owned = Column(Boolean)
    reading_status = Column(String)
    rating = Column(Double)
    sold_by = Column(String)
    location = Column(String)
    purchase_date = Column(Date)
    price_paid = Column(Double)
    reading_date = Column(Date) # Definitely need another reading information table
    amazon_url = Column(String)
    goodreads_url = Column(String)
    librarything_url = Column(String)
    openlibrary_id = Column(String)
    cover_image_link = Column(String)
    reading_priority = Column(String)


    authors = relationship("Author", secondary = book_authors, back_populates="books")

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    display_name = Column(String, nullable = False)

    books = relationship("Book", secondary=book_authors, back_populates="authors")



