from .models import Book, Author    
from rest_framework import serializers
from datetime import datetime

# BookSerializer serializes all fields of the Book model.
# It includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

    class Meta:
        model = Book
        fields = '__all__'
        # Serializes: id, title, publication_year, author

# AuthorSerializer serializes the Author's name and includes a nested list of their books.
# The 'books' field uses BookSerializer to serialize all related Book instances.
# The relationship is handled via the 'related_name' on the Book model's ForeignKey.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        # Serializes: id, name, and a nested list of books

# Relationship explanation:
# - Each Book is linked to an Author via the ForeignKey.
# - AuthorSerializer uses the 'books' related_name to access all books for an author,
#   and serializes them using BookSerializer for nested representation.
