# Advanced Features and Security Django Project

This project demonstrates advanced Django features including:
- Custom user model with extra fields
- Permissions and groups
- Secure settings and HTTPS deployment
- CRUD operations for Book and Document models

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

4. Run the server:
   ```
   python manage.py runserver
   ```

## Features

- Custom user model (`bookshelf.CustomUser`)
- Permissions for documents and books
- Secure settings for production
- Admin interface for managing users and books

## Security Measures

- DEBUG is set to False in production.
- CSRF and session cookies are secured for HTTPS.
- Browser-side protections (XSS filter, content type nosniff, frame options) are enabled.
- All forms include CSRF tokens.
- Data access uses Django ORM and validated forms.
- Content Security Policy (CSP) is enforced using django-csp.

See `SECURITY_REVIEW.md` for details on security best practices.

## Deployment

See `DEPLOYMENT.md` for HTTPS and server configuration instructions.