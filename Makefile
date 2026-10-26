
fetch:
	curl -o akeneo-web-api.json https://converter.swagger.io/api/convert?url=https://raw.githubusercontent.com/akeneo/pim-api-docs/master/content/swagger/akeneo-web-api.json
	

generate:
	openapi-generator generate \
		-i ./akeneo-web-api.json \
		-g python-nextgen \
		--additional-properties=packageName=akeneo,projectName=akeneo-python-sdk,packageUrl=https://github.com/labd/akeneo-python-sdk.git
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
