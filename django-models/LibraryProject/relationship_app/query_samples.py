from .models import Book, Library, Author, Librarian


# Sample query functions to demonstrate relationships

book_by_author = Book.objects.filter(author=author_name)

books_in_library = Library.objects.get(name=library_name).books.all()

librarian_of_library = Librarian.objects.get(library__name=library_name)