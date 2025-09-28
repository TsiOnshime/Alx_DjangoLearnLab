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
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']  # Enable filtering by these fields
    search_fields = ['title', 'author__name']  # Enable search by book title and author name
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
