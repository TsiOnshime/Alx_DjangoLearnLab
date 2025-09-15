from bookshelf.models import Book


# Get all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)


# Get a specific book
book = Book.objects.get(title='black horse')
print(book.title, book.author, book.publication_year)

# Output: 1984 George Orwell 1949