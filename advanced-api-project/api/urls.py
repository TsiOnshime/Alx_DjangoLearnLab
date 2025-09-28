from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),                # GET: List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),   # GET: Retrieve book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),     # POST: Create new book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'), # PUT/PATCH: Update book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'), # DELETE: Delete book
]

# Each endpoint is mapped to its corresponding view.
# Use these endpoints with Postman, curl, or your frontend.
