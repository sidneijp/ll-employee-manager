# employee-manager
___
[![CircleCI](https://circleci.com/bb/sidnei/employee-manager/tree/develop.svg?style=svg)](https://circleci.com/bb/sidnei/employee-manager/tree/develop)

A Django Admin panel to manage employees' data and an API to list, add and remove employees.

## Installation

### Dependecies

- Python 3.6
- Django 2.0
- pipenv 11.10.0

The project uses `pipenv` instead of `pip` to manage python - so there is no `requirements.txt`. To install, run as root:

```# pip install -U pipenv```

Now to install python packages dependencies:

```$ pipenv install```

Apply database migrations:

```$ python manage.py migrate```

Create an user (just follow the instructions) :

```$ python manage.py createsuperuser```

Finally run the application and the API will be available at http://localhost:8000 and the admin interface at http://localhost:8000/admin

```$ python manage.py runserver 0.0.0.0:8000```

### Development

Install the `dev-packages` to be able to run tests, generate coverage report, run linter, etc. 

```$ pipenv install --dev```

To run automated tests:

```$ py.test```

or run in "watcher mode":

```$ ptw```

to generate tests coverage:

```coverage run -m py.test```

then to see the report result:

```coverage report```

or for "HTML fashion" report:

```coverage html```

The HTML report will be available at `./htmlcov/index.html` - open it with a web browser.

## API example (list)

Request
```curl -u username:password -H "Content-Type: application/javascript" http://localhost:8000/employee/```

## Response
```
[
    {
        "name": "Sid",
        "email": "sid@internet.com",
        "department": "Sales"
    },
    {
        "name": "Sidnei",
        "email": "sidnei@internet.com",
        "department": "IT"
    },
    {
        "name": "Ney",
        "email": "ney@internet.com",
        "department": "RH"
    }
]
```
