from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# BookListView:
# - Purpose: Retrieve a list of all Book instances.
# - Permissions: Open to all users (authenticated or not).
# - Endpoint: GET /books/
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view

# BookDetailView:
# - Purpose: Retrieve details of a single Book by its ID.
# - Permissions: Open to all users.
# - Endpoint: GET /books/<int:pk>/
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view

# BookCreateView:
# - Purpose: Create a new Book instance.
# - Permissions: Only authenticated users can create.
# - Endpoint: POST /books/create/
# - Custom Hook: perform_create allows for custom logic during creation.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    def perform_create(self, serializer):
        # Custom logic can be added here (e.g., logging, notifications)
        serializer.save()

# BookUpdateView:
# - Purpose: Update an existing Book instance.
# - Permissions: Only authenticated users can update.
# - Endpoint: PUT/PATCH /books/<int:pk>/update/
# - Custom Hook: perform_update allows for custom logic during update.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    def perform_update(self, serializer):
        # Custom logic can be added here
        serializer.save()

# BookDeleteView:
# - Purpose: Delete a Book instance.
# - Permissions: Only authenticated users can delete.
# - Endpoint: DELETE /books/<int:pk>/delete/
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# --- View Configuration Summary ---
# - List and Detail views are read-only and open to all users.
# - Create, Update, and Delete views require authentication.
# - Custom hooks (perform_create, perform_update) are available for extending default behavior.
# - Permissions are enforced using DRF's permission_classes.
