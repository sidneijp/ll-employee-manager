SHELL:=/bin/bash
PORT:=8000
MANAGE:=`pipenv --venv`/bin/python manage.py

requirements:
	pipenv install

dev-requirements:
	pipenv install --dev

load-initial-data:
	$(MANAGE) loaddata employee_manager/fixtures/auth.json
	$(MANAGE) loaddata core/fixtures/department.json

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
	cp settings.ini.sample settings.ini

dev-install: dev-requirements migrate load-initial-data
	cp settings.ini.sample settings.ini

update:	pull install

dev-update:	pull dev-install
