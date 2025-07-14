Project: Watchmate API (Django REST Framework)
Overview
Watchmate is a Django REST Framework (DRF) based API for managing and reviewing watchlists of movies and streaming platforms. It features user authentication (including JWT and token-based), user registration, and CRUD operations for watchlists, platforms, and reviews.

Features
User Registration & Authentication: Supports both token and JWT authentication for secure API access.
Watchlist Management: Create, read, update, and delete movies and streaming platforms.
Review System: Users can leave reviews and ratings for movies.
Filtering & Pagination: Supports filtering, searching, and paginating watchlists and reviews.
Admin Panel: Django admin for managing models.
Rate Limiting: Throttling for API endpoints to prevent abuse.
Project Structure
watchmate/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── user_app/
│   ├── api/
│   ├── admin.py
│   ├── models.py
│   └── ...
├── watchlist_app/
│   ├── api/
│   ├── admin.py
│   ├── models.py
│   └── ...
├── watchmate/
│   ├── settings.py
│   ├── urls.py
│   └── ...
Installation
Clone the repository:
bash
git clone <repo-url>
cd watchmate
Create a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
bash
pip install -r requirements.txt
Apply migrations:
bash
python manage.py migrate
Create a superuser (optional, for admin):
bash
python manage.py createsuperuser
Run the development server:
bash
python manage.py runserver
API Endpoints
Authentication
POST /account/login/ — Token-based login
POST /account/register/ — Register a new user
POST /account/logout/ — Logout
POST /account/api/token/ — JWT obtain pair
POST /account/api/token/refresh/ — JWT refresh
Watchlists & Platforms
GET /watch/list/ — List all watchlists
GET /watch/<int:pk>/ — Retrieve a single watchlist
POST /watch/list/ — Create a new watchlist (admin)
GET /watch/stream/ — List all streaming platforms
Reviews
GET /watch/<int:pk>/review — List reviews for a watchlist
POST /watch/<int:pk>/review/create — Add a review (authenticated)
GET /watch/review/<int:pk> — Retrieve a review
GET /watch/review/ — List reviews by the current user
Technologies Used
Python 3.x
Django 5.2.3
Django REST Framework
JWT Authentication (djangorestframework_simplejwt)
SQLite (default, can be changed)
Contributing
Fork the repository
Create your feature branch (git checkout -b feature/YourFeature)
Commit your changes
Push to the branch (git push origin feature/YourFeature)
Open a Pull Request
License
This project is licensed under the MIT License.

Contact
For questions or suggestions, open an issue or contact the maintainer.