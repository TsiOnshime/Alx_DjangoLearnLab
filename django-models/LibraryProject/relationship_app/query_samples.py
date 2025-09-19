from .models import Book, Library, Author, Librarian

# Sample query functions to demonstrate relationships

author = Author.objects.get(name=author_name)
book_by_author = Book.objects.filter(author=author)

books_in_library = Library.objects.get(name=library_name).books.all()

library = Library.objects.get(name=library_name)
librarian_of_library = Librarian.objects.get(library=library)