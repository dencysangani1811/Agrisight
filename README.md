# 🌾 Agrisight – Smart Agriculture Django App

**Agrisight** is a web-based Django platform designed to support smart agriculture through crop and disease management insights.

## 🚀 Features
- 🔐 User registration & login
- 📷 Crop disease detection interface (image-based)
- 📊 Visual dashboards (static content)
- 📁 Static and media file support
- 🧠 Backend-ready for AI integration

## 🛠 Tech Stack
- Python 3.x
- Django
- HTML / CSS / JS (static assets)
- SQLite (default)

## 📂 Project Structure

agro/
├── agro/ # Main Django project settings
├── homepage/ # Main app logic: views, models, forms
├── htmlfiles/ # Template HTML files
├── static/ # Static assets (CSS, images, JS)
├── media/ # Uploaded media (excluded from Git)
├── db.sqlite3 # Local development DB
├── manage.py
└── requirements.txt



## ⚙️ Setup Instructions

### 🔹 Clone the repository

git clone git@github.com:dencysangani1811/Agrisight.git
cd Agrisight


🔹 Create virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


🔹 Install dependencies

pip install -r requirements.txt



🔹 Run the server

python manage.py migrate
python manage.py runserver


📌 Notes
Make sure to collect media files and set up static properly for production

Default DB is SQLite for development on
