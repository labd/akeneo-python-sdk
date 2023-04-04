# Improvements

As the Swagger documentation of Akeneo is not 100% correct, some (manual) improvements are listed here.

## Fetching

This repo contains the updated akeneo-web-api.json, which includes the manual changes listed below. In case you want to retrieve the latest version of the Swagger documentation, run the following:

```make fetch```


### manual adjustments
See https://github.com/labd/akeneo-node-sdk/blob/main/IMPROVEMENTS.md for more improvements

### OpenAPI generate problems
Issue when trying to get products from the api. Fixed by setting `ProductsEmbeddedItemsInnerAllOf1ValuesValueInner` `data` property to `any` instead of `Dict[str, Any]`

Issue when trying to get products from the api. `dict has no attribute "from_dict"` Fixed by changing line 120 from `Products1EmbeddedItemsInner` to `"values": dict((_k, [ProductsEmbeddedItemsInnerAllOf1ValuesValueInner.from_dict(_item) for _item in _v]) for _k, _v in obj.get("values").items()),`
Same for line 122 of ProductsEmbeddedItemsInner

Issue when getting assets. Same issue as above. Fixed by Changing line 79 from `AssetEmbeddedItemsInnerAllOf` to `"values": dict((_k, [AssetEmbeddedItemsInnerAllOfValuesValueInner.from_dict(_item) for _item in _v]) for _k, _v in obj.get("values").items()), `