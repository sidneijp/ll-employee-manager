SHELL:=/bin/bash
PORT:=8000
MANAGE:=`pipenv --venv`/bin/python manage.py

requirements:
	pipenv install

dev-requirements:
	pipenv install --dev

load-initial-data:
	$(MANAGE) loaddata employee_manager/fixtures/auth.json

run:
	$(MANAGE) runserver 0.0.0.0:$(PORT)

migrate:
	$(MANAGE) migrate

collectstatic:
	$(MANAGE) collectstatic --noinput

shell:
	$(MANAGE) shell

test:
	py.test

testd:
	ptw

coverage:
	coverage run -m py.test

report:
	coverage report

html:
	@coverage html
	@echo "Generated coverage HTML report at ./htmlcov"

clean:
	@rm -f .coverage
	@rm -rf htmlcov/
	@echo "Cleaned coverage report files"

pull:
	git pull origin

install: requirements migrate load-initial-data

dev-install: dev-requirements migrate load-initial-data

update:	pull install load-initial-data

dev-update:	pull dev-install load-initial-data
