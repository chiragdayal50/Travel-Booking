# Travel Booking Web Application

## Project Description
This is a Django-based travel booking web application using Aiven as the SQL database. The application allows users to register, log in, view travel options, book tickets, and manage their bookings.


## Features
- User authentication (Register, Login, Logout)
- Browse available travel options
- Book travel tickets
- View and manage bookings
- Cancel bookings

## Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Git
- Any SQL-compatible database

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/chiragdayal50/Travel-Booking
cd travel-booking
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
Update `settings.py` with your database connection details:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Deployment
- Ensure the database is set up in a production environment.
- Use Gunicorn and Nginx for deployment.
- Configure `ALLOWED_HOSTS` and `DEBUG = False` in `settings.py`.
- Use `python manage.py collectstatic` to collect static files.

## Contributing
Feel free to fork the repository and submit pull requests.
