# Django Project

Django project created for practice.

## Installation

Create a virtual environment (MAC/Linux):

```bash
python3 -m venv DjangoAssignment
```

Activate the virtual environment:

```bash
source DjangoAssignment/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

## Run
Navigate to LoginSystem directory : `cd LoginSystem`

Start server:
```bash
python manage.py runserver
```

## Available end points

Available end points can be viewed via postman. Import `Django Project.postman_collection.json` file located inside Postman directory. Set enviornment variable `api_url` to local url; defaults to `http://localhost:8000`

* **Loginify Home:**
    * **Method:** `GET`
    * **Endpoint:** `{{api_url}}/login/home`
    * **Description:** A simple test endpoint that returns a welcome message.

## Available routes
**`{{api_url}}/signup`**:

Accepts username, email and password. Email must be unique. Cannot be accessed via postman due to CSRF block.

**`{{api_url}}/login`**:

Accepts email and password to login.

## Superuser

Log in with:

Username: `kushalghimire`

Pasword: `123456`