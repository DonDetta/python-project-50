lint:
	uv run ruff check gendiff tests

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml