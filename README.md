# 📚 Django Book Catalog API

A RESTful API for managing a book catalog system with authentication, file uploads, and Postman test support.

---

## 🚀 Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/django-book-catalog-api.git
   cd django-book-catalog-api
   ```
2. **Start Python Virtual Enviorment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```

## 🔐 API Key Authentication

### Configuration in your .env file:

VALID_API_KEYS=valid-key

In settings.py, it will read:

VALID_API_KEYS = env("VALID_API_KEYS", default="valid-key").split(",")

### 📬 How to Use:

Send this header in Postman:

Key:   X-API-Key
Value: valid-key

## 📸 Screenshots of 5 Key Postman Tests

### 1️⃣ Create Book (Valid Data)
![Create Book](screenshots/Test-1.png)

### 2️⃣ Upload Valid Cover Image
![Upload Valid Cover](screenshots/Test-2.png)

### 3️⃣ Get Book with Cover
![Get Book](screenshots/Test-3.png)

### 4️⃣ Invalid API Key Test
![Invalid API](screenshots/Test-4.png)

### 5️⃣ Invalid File Type (400)
![Invalid File Tyoe](screenshots/Test-5.png)

