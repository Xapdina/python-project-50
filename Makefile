install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

tests-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
	export CC_TEST_REPORTER_ID=ваш_идентификатор
    /home/runner/work/python-project-50/python-project-50/cc-reporter before-build
    /usr/bin/make tests-coverage
