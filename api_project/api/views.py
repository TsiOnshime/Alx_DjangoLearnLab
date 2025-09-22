from django.shortcuts import render
from rest_framework import generics, viewsets, permissions

# Create your views here.

from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Only authenticated users can create, update, or delete books.
# Unauthenticated users can only read (GET) book data.
