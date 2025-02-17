from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schema, crud
from app.db import SessionLocal

# Create FastAPI instance
fast = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root route
@fast.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Bookstore!"}

# Create a new book
@fast.post("/books/", response_model=schema.Book)
def create_book(book: schema.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

# Get all books
@fast.get("/books/", response_model=list[schema.Book])
def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db=db, skip=skip, limit=limit)

# Get a specific book by ID
@fast.get("/books/{book_id}", response_model=schema.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Update a book
@fast.put("/books/{book_id}", response_model=schema.Book)
def update_book(book_id: int, book: schema.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db=db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Delete a book
@fast.delete("/books/{book_id}", response_model=schema.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
