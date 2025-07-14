# 🎬 Watchmate API (DRF)

Watchmate is a Django REST Framework (DRF) based API for managing and reviewing watchlists of movies and streaming platforms. It features user authentication (JWT and token-based), user registration, and CRUD operations for watchlists, platforms, and reviews.

---

## 🚀 Features

- **User Registration & Authentication**: Token and JWT-based secure access.
- **Watchlist Management**: Create, read, update, and delete movies and platforms.
- **Review System**: Users can add reviews and ratings for movies.
- **Filtering & Pagination**: Filter, search, and paginate data.
- **Admin Panel**: Manage models via Django admin.
- **Rate Limiting**: Throttling to prevent API abuse.

---

## 🔗 API Endpoints

### 🔐 Authentication
- `POST /account/login/` — Token-based login  
- `POST /account/register/` — Register a new user  
- `POST /account/logout/` — Logout  
- `POST /account/api/token/` — JWT obtain pair  
- `POST /account/api/token/refresh/` — JWT refresh  

### 📺 Watchlists & Platforms
- `GET /watch/list/` — List all watchlists  
- `GET /watch/<int:pk>/` — Retrieve a single watchlist  
- `POST /watch/list/` — Create a new watchlist (admin only)  
- `GET /watch/stream/` — List all streaming platforms  

### 📝 Reviews
- `GET /watch/<int:pk>/review/` — List reviews for a watchlist  
- `POST /watch/<int:pk>/review/create/` — Add a review (authenticated)  
- `GET /watch/review/<int:pk>/` — Retrieve a review  
- `GET /watch/review/` — List reviews by the current user  
