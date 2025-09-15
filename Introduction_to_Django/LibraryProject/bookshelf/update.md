from bookshelf.models import Book


# Get book with title 1984

book = Book.objects.get(title='1984')

# change title

book.title = 'Nineteen Eighty-Four'

book.save()

print(book.title)
# Output: Nineteen Eighty-Four