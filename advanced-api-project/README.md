# API View Configuration

## Endpoints

- `GET /books/`  
  Returns a list of all books. Open to all users.

- `GET /books/<int:pk>/`  
  Returns details for a specific book by ID. Open to all users.

- `POST /books/create/`  
  Creates a new book. Requires authentication.

- `PUT/PATCH /books/<int:pk>/update/`  
  Updates an existing book. Requires authentication.

- `DELETE /books/<int:pk>/delete/`  
  Deletes a book. Requires authentication.

## Permissions

- **List & Detail:** Anyone can view.
- **Create, Update, Delete:** Only authenticated users.

## Custom Hooks

- `perform_create(self, serializer)`: Extend logic during book creation.
- `perform_update(self, serializer)`: Extend logic during book update.

## How to Test

Use Postman, curl, or Django's browsable API to interact with endpoints.  
Test with and without authentication to verify permissions.

## Notes

- All views use Django REST Framework generic views for simplicity and maintainability.
- Permissions are enforced using DRF's built-in permission classes.



## Filtering, Searching, and Ordering

### Filtering
Filter books by title, author, or publication year:
```
GET /api/books/?title=Emma&publication_year=1815
```

### Searching
Search books by title or author's name:
```
GET /api/books/?search=Austen
```

### Ordering
Order books by title or publication year:
```
GET /api/books/?ordering=publication_year
GET /api/books/?ordering=-title
```
