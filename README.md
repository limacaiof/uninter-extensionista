<div align="center">

# Prato Solidário

A simple website designed to manage and promote social actions aimed at combating hunger.

</div>

# Overview

Prato Solidário is a web platform designed to manage and promote social actions aimed at combating hunger. This project is developed as part of the extension activities at [UNINTER](https://www.uninter.com/) University. Our mission is to connect communities and organizations to facilitate support and raise awareness about food insecurity.

## Technologies Used

- **Framework**: Django
- **Frontend**: HTML5, CSS, Bootstrap
- **Backend**: Python
- **Database**: MariaDB

## Getting started

### Docker

1. Run the Docker compose command to build the project and the database:
   ```bash
   docker compose up
   ```
1. Run the migrations to setup the project database structure:
    ```bash
    docker exec -it app-prato-solidario python manage.py migrate
    ```
2. Start the development server:
    ```bash
    docker exec -it app-prato-solidario python manage.py runserver 0.0.0.0:8000
    ```
### Virtual Environment

1. Install the dependencies with pip
    ```bash
    pip install -r requirements.txt
    ```
2. Copy the content of `.env.example` file to a new `.env` and change the values in order to work with your MariaDB.

    2.1. If you don't want to configure a database, add this code snippet to the end of the `settings.py` file to use a sqlite3 database to run the application.
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ``` 
3. Run the migrations to set the structure of the database:
    ```bash
    python manage.py migrate
    ```

4. Start the development server:
    ```bash
    python manage.py runserver
    ```