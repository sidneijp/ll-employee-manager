activate:
	pipenv shell --three

requirements:
	pipenv install

dev-requirements:
	pipenv install --dev

runserver:
	python manage.py runserver

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --noinput

shell:
	python manage.py shell

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
