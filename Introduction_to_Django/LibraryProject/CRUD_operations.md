from bookshelf.models import Book


book = Book(title='1984', author='George Orwell',publication_year=1949)

book.save()

# Output: Book object created with id=1


from bookshelf.models import Book


# Get all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)


# Get a specific book
book = Book.objects.get(title='black horse')
print(book.title, book.author, book.publication_year)

# Output: 1984 George Orwell 1949


from bookshelf.models import Book


# Get book with title 1984

book = Book.objects.get(title='1984')

# change title

book.title = 'Nineteen Eighty-Four'

book.save()

print(book.title)
# Output: Nineteen Eighty-Four


from bookshelf.models import Book

# delete a book

book = Book.objects.get(author='George Orwell')

book.delete()

print(list(books))
# Output: []