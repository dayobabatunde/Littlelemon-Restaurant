# 🍋 Little Lemon Restaurant API

This project is a **Django REST Framework (DRF)** application that exposes APIs for managing **menu items** and **table bookings** for the Little Lemon restaurant.  
It connects to a **MySQL database**, supports **user registration and authentication via Djoser**, and includes **unit tests** to ensure correctness.  
The API can be tested using clients such as **Insomnia** or **Postman**.

---

## ✅ Features

- Django backend with DRF  
- MySQL database integration  
- Menu and table booking APIs (CRUD)  
- User registration and token authentication (Djoser)  
- Static HTML served via Django  
- Unit tests for API validation  
- Token-based authentication tested with Insomnia  

---

## 🔗 API Routes

### Static HTML
- `GET /restaurant/` → Returns the index/static HTML page.  

### Admin
- `GET /admin/` → Django admin (requires superuser).  

### Menu API
- `GET /restaurant/menu/` → List all menu items.  
- `POST /restaurant/menu/` → Create a menu item.  
- `GET /restaurant/menu/<int:pk>` → Retrieve a single menu item.  
- `PUT /restaurant/menu/<int:pk>` → Update a menu item.  
- `PATCH /restaurant/menu/<int:pk>` → Partial update.  
- `DELETE /restaurant/menu/<int:pk>` → Delete a menu item.  

### Table Booking API (ViewSet)
- `GET /restaurant/booking/tables/` → List all bookings.  
- `POST /restaurant/booking/tables/` → Create a booking.  
- `GET /restaurant/booking/tables/<int:pk>/` → Retrieve a booking.  
- `PUT /restaurant/booking/tables/<int:pk>/` → Update a booking.  
- `PATCH /restaurant/booking/tables/<int:pk>/` → Partial update.  
- `DELETE /restaurant/booking/tables/<int:pk>/` → Delete a booking.  

### Authentication & User Registration (Djoser)
- `POST /auth/users/` → Register a new user.  
- `GET /auth/users/me/` → Retrieve logged-in user profile (requires auth).  
- `POST /auth/token/login/` → Obtain authentication token.  

**Example request body:**
```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
