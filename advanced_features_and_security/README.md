# advanced_features_and_security

This project is a Django application that customizes the user model to include additional features and security enhancements.

## Features

- Custom user model extending `AbstractUser`
- Additional fields: 
  - `date_of_birth`: DateField for storing the user's date of birth.
  - `profile_photo`: ImageField for storing the user's profile photo.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd advanced_features_and_security
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Admin interface available at `http://127.0.0.1:8000/admin/` (create a superuser to access)

## Permissions & Groups Setup

- Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) are defined in the Document model.
- Groups (Editors, Viewers, Admins) can be managed in Django admin.
- Views are protected using `@permission_required`.
- Assign users to groups and permissions in admin to control access.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.