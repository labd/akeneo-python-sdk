# Improvements

As the Swagger documentation of Akeneo is not 100% correct, some (manual) improvements are listed here.

## Fetching

This repo contains the updated akeneo-web-api.json, which includes the manual changes listed below. In case you want to retrieve the latest version of the Swagger documentation, run the following:

```make fetch```


### manual adjustments
See https://github.com/labd/akeneo-node-sdk/blob/main/IMPROVEMENTS.md for more improvements

Changed 
```json
"properties": {
    "localeCode": {
        "type": "string",
        "description": "Category label for the locale `localeCode`"
    }
}
``` 
and
```json
"properties": {
    "localeCode": {
        "type": "string",
        "description": "Attribute label for the locale `localeCode`"
    }
}
```

to 

```json
"additionalProperties": {
    "type": "string"
},
```

Changed ```
"associations": {
                                      "type": "object",
                                      "properties": {
                                        "associationTypeCode": {
                                          "type": "object",
                                          "properties": {
                                            "groups": {
                                              "type": "array",
                                              "description": "Array of groups codes with which the product is in relation",
                                              "items": {
                                                "type": "string"
                                              }
                                            },
                                            "products": {
                                              "type": "array",
                                              "description": "Array of product identifiers with which the product is in relation",
                                              "items": {
                                                "type": "string"
                                              }
                                            },
                                            "product_models": {
                                              "type": "array",
                                              "description": "Array of product model codes with which the product is in relation (only available since the v2.1)",
                                              "items": {
                                                "type": "string"
                                              },
                                              "x-from-version": "2.1"
                                            }
                                          }
                                        }
                                      },```

To ```
"associations": {
                                    "type": "object",
                                    "additionalProperties": {
                                          "type": "object",
                                          "properties": {
                                            "groups": {
                                              "type": "array",
                                              "description": "Array of groups codes with which the product is in relation",
                                              "items": {
                                                "type": "string"
                                              }
                                            },
                                            "products": {
                                              "type": "array",
                                              "description": "Array of product identifiers with which the product is in relation",
                                              "items": {
                                                "type": "string"
                                              }
                                            },
                                            "product_models": {
                                              "type": "array",
                                              "description": "Array of product model codes with which the product is in relation (only available since the v2.1)",
                                              "items": {
                                                "type": "string"
                                              },
                                              "x-from-version": "2.1"
                                            }
                                        
                                      }
                                    },
```

### OpenAPI generate problems
Issues with data property on serveral classes. Fixed by searching `data: Dict[str, any]` and replacing all to `data: Any`

Issue when trying to get products from the api. `dict has no attribute "from_dict"` Fixed by changing line 120 from `Products1EmbeddedItemsInner` to `"values": dict((_k, [ProductsEmbeddedItemsInnerAllOf1ValuesValueInner.from_dict(_item) for _item in _v]) for _k, _v in obj.get("values").items()),`
Same for line 122 of ProductsEmbeddedItemsInner

Issue when getting assets. Same issue as above. Fixed by Changing line 79 from `AssetEmbeddedItemsInnerAllOf` to `"values": dict((_k, [AssetEmbeddedItemsInnerAllOfValuesValueInner.from_dict(_item) for _item in _v]) for _k, _v in obj.get("values").items()), `
Set `data` from `AssetEmbeddedItemsInnerAllOfValuesValueInner` to any as well.

Issues with associations; Fixed by changing line 127 from `ProductsEmbeddedItemsInner` to `            "associations": dict((_k, ProductsEmbeddedItemsInnerAllOf1AssociationsValue.from_dict(_v)) for _k, _v in obj.get("associations").items()),`