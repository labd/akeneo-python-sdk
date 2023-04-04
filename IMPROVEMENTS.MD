# Improvements

As the Swagger documentation of Akeneo is not 100% correct, some (manual) improvements are listed here.

## Fetching

This repo contains the updated akeneo-web-api.json, which includes the manual changes listed below. In case you want to retrieve the latest version of the Swagger documentation, run the following:

```make fetch```


### manual adjustments
See https://github.com/labd/akeneo-node-sdk/blob/main/IMPROVEMENTS.md for more improvements

### OpenAPI generate problems
Issue when trying to get products from the api. Fixed by setting `ProductsEmbeddedItemsInnerAllOf1ValuesValueInner` `data` property to `any` instead of `Dict[str, Any]`

