from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'Books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)


# create db file
engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)

# session
Session = sessionmaker(bind=engine)
session = Session()

# insert books
insert_books = [
    Book(title="The Book Thief", year=2006),
    Book(title="Don Quixote", year=1605),
    Book(title="American Psycho", year=2022),
]

session.add_all(insert_books)
session.commit()

# read books
books = session.query(Book).all()

# display
for book in books:
    print(f"ID: {book.id}, Title: {book.title}, Year: {book.year}")

session.close()