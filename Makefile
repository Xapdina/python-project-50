install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

tests-coverage:
	export CC_TEST_REPORTER_ID=dbdb9236310d56aa44d69c635f232f5f36c4aa277d4a8db79aa768e2a5d72a0d
	poetry run pytest --cov=gendiff --cov-report xml


