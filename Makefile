
fetch:
	curl -o akeneo-web-api.json https://converter.swagger.io/api/convert?url=https://raw.githubusercontent.com/akeneo/pim-api-docs/master/content/swagger/akeneo-web-api.json
	

generate:
	openapi-generator generate \
		-i ./akeneo-web-api.json \
		-g python-nextgen \
		--additional-properties=packageName=akeneo,projectName=akeneo-python-sdk,packageUrl=https://github.com/labd/akeneo-python-sdk.git \