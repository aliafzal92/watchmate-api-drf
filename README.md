Here is your `README.md` properly formatted for GitHub:

```markdown
# 🎬 Watchmate API (Django REST Framework)

**Watchmate** is a Django REST Framework (DRF) based API for managing and reviewing watchlists of movies and streaming platforms. It includes user authentication (JWT and token-based), user registration, and full CRUD functionality for watchlists, platforms, and reviews.

---

## 🚀 Features

- **User Registration & Authentication**  
  Supports both **Token** and **JWT** authentication for secure API access.

- **Watchlist Management**  
  Create, read, update, and delete movies and streaming platforms.

- **Review System**  
  Users can leave reviews and ratings for movies.

- **Filtering & Pagination**  
  Filter, search, and paginate through watchlists and reviews.

- **Admin Panel**  
  Django admin interface for managing models.

- **Rate Limiting**  
  Throttling for API endpoints to prevent abuse.

---

## 🗂 Project Structure

```

watchmate/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── user\_app/
│   ├── api/
│   ├── admin.py
│   ├── models.py
│   └── ...
├── watchlist\_app/
│   ├── api/
│   ├── admin.py
│   ├── models.py
│   └── ...
├── watchmate/
│   ├── settings.py
│   ├── urls.py
│   └── ...

````

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/watchmate-drf.git
cd watchmate
````

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (optional)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints

### 🔐 Authentication

| Method | Endpoint                      | Description           |
| ------ | ----------------------------- | --------------------- |
| POST   | `/account/login/`             | Token-based login     |
| POST   | `/account/register/`          | Register a new user   |
| POST   | `/account/logout/`            | Logout                |
| POST   | `/account/api/token/`         | JWT obtain token pair |
| POST   | `/account/api/token/refresh/` | JWT refresh token     |

### 📺 Watchlists & Platforms

| Method | Endpoint           | Description                    |
| ------ | ------------------ | ------------------------------ |
| GET    | `/watch/list/`     | List all watchlists            |
| GET    | `/watch/<int:pk>/` | Retrieve a single watchlist    |
| POST   | `/watch/list/`     | Create a new watchlist (admin) |
| GET    | `/watch/stream/`   | List all streaming platforms   |

### 📝 Reviews

| Method | Endpoint                         | Description                      |
| ------ | -------------------------------- | -------------------------------- |
| GET    | `/watch/<int:pk>/review/`        | List reviews for a watchlist     |
| POST   | `/watch/<int:pk>/review/create/` | Add a review (authenticated)     |
| GET    | `/watch/review/<int:pk>/`        | Retrieve a review                |
| GET    | `/watch/review/`                 | List reviews by the current user |

---

## 🛠 Technologies Used

* Python 3.x
* Django 5.2.3
* Django REST Framework
* JWT Authentication (`djangorestframework_simplejwt`)
* SQLite (default database, can be replaced)

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:

   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes
4. Push to the branch:

   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

For questions, suggestions, or issues, feel free to [open an issue](https://github.com/yourusername/watchmate-drf/issues) or contact the maintainer.

```

> ✅ **Tip**: Replace `yourusername` with your actual GitHub username or organization name in the clone URL and issue link.

Let me know if you'd like a badge section (build status, license, etc.) or a live demo link.
```
