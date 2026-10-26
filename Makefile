
fetch:
	curl -o akeneo-web-api.json https://converter.swagger.io/api/convert?url=https://raw.githubusercontent.com/akeneo/pim-api-docs/master/content/swagger/akeneo-web-api.json
	

generate:
	openapi-generator generate \
		-i ./akeneo-web-api.json \
		-g python-nextgen \
		--additional-properties=packageName=akeneo,projectName=akeneo-python-sdk,packageUrl=https://github.com/labd/akeneo-python-sdk.git
	# The version lives in pyproject.toml only (managed by knope). Also re-apply
	# the importlib.metadata version in configuration.py to_debug_report().
	perl -pi -e 's/^__version__ = .*/from importlib.metadata import version as _package_version\n\n__version__ = _package_version("akeneo-python-sdk")/' akeneo/__init__.py
	uv run ruff check --fix akeneo test
	uv run ruff format akeneo test

format:
	uv run ruff check --fix akeneo test
	uv run ruff format akeneo test

lint:
	uv run ruff format --check akeneo test
	uv run ruff check akeneo test

test:
	uv run pytest
