from .models import Book, Library, Author, Librarian


# Sample query functions to demonstrate relationships

book_by_author = Book.objects.filter(author="james")

books_in_library = Library.objects.get(name="Central Library").books.all()

librarian_of_library = Librarian.objects.get(library__name="Central Library")