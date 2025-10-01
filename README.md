# 🍋 Little Lemon Restaurant API

This project is a Django REST Framework (DRF) application...

---

## ✅ Features
- Django backend with DRF
- MySQL database integration
- Menu and table booking APIs (CRUD)

---

## 🔗 API Routes

### Menu API
- `GET /restaurant/menu/` → List all menu items.
- `POST /restaurant/menu/` → Create a menu item.
- `GET /restaurant/menu/<int:pk>` → Retrieve a single menu item.

---

### Authentication & User Registration (Djoser)
- `POST /auth/users/` → Register a new user.
- `POST /auth/token/login/` → Obtain authentication token.

**Authorization Header for Protected Endpoints:**  
