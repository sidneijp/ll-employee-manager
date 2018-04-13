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

```$ make install```

To the application and the API will be available at http://localhost:8000 and the admin interface at http://localhost:8000/admin.

```$ make run```

A initial superuser is created:

```
username:admin

password:employee123

```

### Development

Install the `dev-packages` to be able to run tests, generate coverage report, run linter, etc. 

```$ make dev-install```

To run automated tests:

```$ make test```

or run in "watcher mode":

```$ make testd```

to generate tests coverage:

```$ make coverage```

then to see the report result:

```make report```

or for "HTML fashion" report:

```make html```

*The HTML report will be available at `./htmlcov/index.html` - open it with a web browser.

## API example (list)

URL schema:

```http://localhost:8000/employee/[employee_email/][?department=department_name]```

with curl
```curl -u username:password -H "Content-Type: application/json" http://localhost:8000/employee/[employee_email/][?department=department_name]```


### Examples

To create some employees:

```curl -u admin:employee123 -X POST -d '{"name": "Jack", "email": "jack@test.com", "department":"IT"}' -H "Content-Type: application/json" http://localhost:8000/employee/'```

```curl -u admin:employee123 -X POST -d '{"name": "John", "email": "john@test.com", "department":"IT"}' -H "Content-Type: application/json" http://localhost:8000/employee/'```

To edit a employee:

```curl -u admin:employee123 -X PUT -d '{"name": "Jackson", "email": "jackson@test.org", "department":"RH"}' -H "Content-Type: application/json" http://localhost:8000/employee/jack@test.com/```

To get a employee:

```curl -u admin:employee123 -X GET -H "Content-Type: application/json" http://localhost:8000/employee/jackson@test.org/```

To list all employees:

```curl -u admin:employee123 -X GET -H "Content-Type: application/json" http://localhost:8000/employee/```

*Response sample: 

```
[
    {
        "name": "Jackson",
        "email": "jackson@test.org",
        "department": "RH"
    },
    {
        "name": "John",
        "email": "john@test.com",
        "department": "IT"
    }
]
```

To list all employees by department:

```curl -u admin:employee123 -X GET -H "Content-Type: application/json" http://localhost:8000/employee/?department=IT```

To delete a employee:

```curl -u admin:employee123 -X DELETE -H "Content-Type: application/json" http://localhost:8000/employee/jackson@test.org/```