from django.db import models

# Author model represents a writer with a name.
# Each Author can have multiple Books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model represents a book with a title, publication year, and a reference to its Author.
# The 'author' field establishes a ForeignKey relationship to Author,
# meaning each Book is linked to one Author, but an Author can have many Books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title