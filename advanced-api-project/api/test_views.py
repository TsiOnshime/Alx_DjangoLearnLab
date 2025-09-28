from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create an author and a book
        self.author = Author.objects.create(name='Jane Austen')
        self.book = Book.objects.create(title='Emma', publication_year=1815, author=self.author)
        self.book_url = reverse('book-detail', args=[self.book.id])
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Emma', str(response.data))

    def test_create_book_requires_auth(self):
        data = {'title': 'Pride and Prejudice', 'publication_year': 1813, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.login(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Pride and Prejudice')

    def test_update_book_requires_auth(self):
        data = {'title': 'Emma Updated', 'publication_year': 1815, 'author': self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Emma Updated')

    def test_delete_book_requires_auth(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=Emma')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Emma')

    def test_search_books_by_author(self):
        response = self.client.get(self.list_url + '?search=Jane')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author.id)

    def test_order_books_by_publication_year(self):
        # Add another book for ordering test
        Book.objects.create(title='Persuasion', publication_year=1817, author=self.author)
        response = self.client.get(self.list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

"""
Testing Documentation:
- This test suite covers CRUD operations, filtering, searching, and ordering for the Book API.
- Authentication and permission checks are included for create, update, and delete endpoints.
- To run tests: python manage.py test api
- Review output for failures and fix any issues.
"""
