from bookshelf.models import Book

# delete a book

book = Book.objects.get(author='George Orwell')

book.delete()

print(list(books))
# Output: []