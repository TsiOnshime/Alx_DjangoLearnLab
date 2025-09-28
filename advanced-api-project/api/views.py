from django_filters import rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# BookListView:
# - Purpose: Retrieve a list of all Book instances.
# - Permissions: Open to all users (authenticated or not).
# - Filtering: Allows filtering by title, author, and publication_year.
# - Endpoint: GET /books/
# BookListView:
# - Purpose: Retrieve a list of all Book instances.
# - Permissions: Open to all users (authenticated or not).
# - Filtering, Searching, Ordering: Enabled for flexible queries.
# - Endpoint: GET /books/
# - Examples:
#     /api/books/?ordering=title
#     /api/books/?ordering=-publication_year
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view
    filter_backends = [filters.OrderingFilter]  # <-- Enable ordering
    ordering_fields = ['title', 'publication_year', 'id', 'author']  # Allow ordering by these fields
    ordering = ['title']  # Default ordering

# DetailView: Retrieves a single book by ID. Read-only for unauthenticated users.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can view

# CreateView: Adds a new book. Only authenticated users can create.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Auth required

    def perform_create(self, serializer):
        serializer.save()

# UpdateView: Modifies an existing book. Only authenticated users can update.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Auth required

    def perform_update(self, serializer):
        serializer.save()

# DeleteView: Removes a book. Only authenticated users can delete.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Auth required

# Each view uses DRF generic views for efficient CRUD operations.
# Permissions are set so only authenticated users can create, update, or delete books.
# List and detail views are open to all users (read-only).
