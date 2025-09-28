from rest_framework import generics, permissions
from .models import Book
from .serializer import BookSerializer

# ListView: Retrieves all books. Read-only for unauthenticated users.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view

# DetailView: Retrieves a single book by ID. Read-only for unauthenticated users.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view

# CreateView: Adds a new book. Only authenticated users can create.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    # Custom behavior: You can override perform_create for extra logic
    def perform_create(self, serializer):
        # Example: Add custom logic here if needed
        serializer.save()

# UpdateView: Modifies an existing book. Only authenticated users can update.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    # Custom behavior: You can override perform_update for extra logic
    def perform_update(self, serializer):
        # Example: Add custom logic here if needed
        serializer.save()

# DeleteView: Removes a book. Only authenticated users can delete.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# Each view uses DRF generic views for efficient CRUD operations.
# Permissions are set so only authenticated users can create, update, or delete books.
# List and detail views are open to all users.