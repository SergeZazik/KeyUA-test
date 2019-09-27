# KeyAU test task

Test task for KeyUA

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Using

- Python 3.7 :snake:
- Django 2.2

### Installing

First of all you need to clone the project
```
git clone https://github.com/SergeZazik/KeyUA-test.git
```

#### Raw python

- It's recommended to create and use [virtual environment](https://docs.python.org/3/library/venv.html)
- Install requirements
    ```
    pip install -r requirements.txt
    ```
- Apply migrations
    ```
    python manage.py migrate
    ```
- Run the server
    ```
    python manage.py runserver
    ```