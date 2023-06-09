# coding: utf-8

# flake8: noqa

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from akeneo.api.asset_api import AssetApi
from akeneo.api.asset_attribute_api import AssetAttributeApi
from akeneo.api.asset_attribute_option_api import AssetAttributeOptionApi
from akeneo.api.asset_family_api import AssetFamilyApi
from akeneo.api.asset_media_file_api import AssetMediaFileApi
from akeneo.api.association_type_api import AssociationTypeApi
from akeneo.api.attribute_api import AttributeApi
from akeneo.api.attribute_group_api import AttributeGroupApi
from akeneo.api.attribute_option_api import AttributeOptionApi
from akeneo.api.authentication_api import AuthenticationApi
from akeneo.api.catalog_products_api import CatalogProductsApi
from akeneo.api.catalogs_api import CatalogsApi
from akeneo.api.category_api import CategoryApi
from akeneo.api.channel_api import ChannelApi
from akeneo.api.currency_api import CurrencyApi
from akeneo.api.family_api import FamilyApi
from akeneo.api.family_variant_api import FamilyVariantApi
from akeneo.api.locale_api import LocaleApi
from akeneo.api.measure_family_api import MeasureFamilyApi
from akeneo.api.measurement_family_api import MeasurementFamilyApi
from akeneo.api.overview_api import OverviewApi
from akeneo.api.pam_asset_api import PAMAssetApi
from akeneo.api.pam_asset_category_api import PAMAssetCategoryApi
from akeneo.api.pam_asset_reference_file_api import PAMAssetReferenceFileApi
from akeneo.api.pam_asset_tag_api import PAMAssetTagApi
from akeneo.api.pam_asset_variation_file_api import PAMAssetVariationFileApi
from akeneo.api.product_identifier_api import ProductIdentifierApi
from akeneo.api.product_uuid_api import ProductUuidApi
from akeneo.api.product_media_file_api import ProductMediaFileApi
from akeneo.api.product_model_api import ProductModelApi
from akeneo.api.published_product_api import PublishedProductApi
from akeneo.api.reference_entity_api import ReferenceEntityApi
from akeneo.api.reference_entity_attribute_api import ReferenceEntityAttributeApi
from akeneo.api.reference_entity_attribute_option_api import ReferenceEntityAttributeOptionApi
from akeneo.api.reference_entity_media_file_api import ReferenceEntityMediaFileApi
from akeneo.api.reference_entity_record_api import ReferenceEntityRecordApi
from akeneo.api.system_api import SystemApi

# import ApiClient
from akeneo.api_client import ApiClient
from akeneo.configuration import Configuration
from akeneo.exceptions import OpenApiException
from akeneo.exceptions import ApiTypeError
from akeneo.exceptions import ApiValueError
from akeneo.exceptions import ApiKeyError
from akeneo.exceptions import ApiAttributeError
from akeneo.exceptions import ApiException
# import models into sdk package
from akeneo.models.app_catalog_list import AppCatalogList
from akeneo.models.app_catalog_list_all_of import AppCatalogListAllOf
from akeneo.models.asset import Asset
from akeneo.models.asset_embedded import AssetEmbedded
from akeneo.models.asset_embedded_items_inner import AssetEmbeddedItemsInner
from akeneo.models.asset_embedded_items_inner_all_of import AssetEmbeddedItemsInnerAllOf
from akeneo.models.asset_embedded_items_inner_all_of_values_value_inner import AssetEmbeddedItemsInnerAllOfValuesValueInner
from akeneo.models.asset_families import AssetFamilies
from akeneo.models.asset_families_embedded import AssetFamiliesEmbedded
from akeneo.models.asset_families_embedded_items_inner import AssetFamiliesEmbeddedItemsInner
from akeneo.models.asset_families_embedded_items_inner_all_of import AssetFamiliesEmbeddedItemsInnerAllOf
from akeneo.models.asset_families_embedded_items_inner_all_of_labels import AssetFamiliesEmbeddedItemsInnerAllOfLabels
from akeneo.models.asset_families_embedded_items_inner_all_of_naming_convention import AssetFamiliesEmbeddedItemsInnerAllOfNamingConvention
from akeneo.models.asset_families_embedded_items_inner_all_of_product_link_rules_inner import AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner
from akeneo.models.asset_families_embedded_items_inner_all_of_product_link_rules_inner_assign_assets_to_inner import AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInnerAssignAssetsToInner
from akeneo.models.asset_families_embedded_items_inner_all_of_product_link_rules_inner_product_selections_inner import AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInnerProductSelectionsInner
from akeneo.models.asset_families_embedded_items_inner_all_of_transformations_inner import AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner
from akeneo.models.asset_families_embedded_items_inner_all_of_transformations_inner_operations import AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerOperations
from akeneo.models.asset_families_embedded_items_inner_all_of_transformations_inner_operations_parameters import AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerOperationsParameters
from akeneo.models.asset_families_embedded_items_inner_all_of_transformations_inner_source import AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerSource
from akeneo.models.asset_families_embedded_items_inner_all_of_transformations_inner_target import AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerTarget
from akeneo.models.asset_family_item_list import AssetFamilyItemList
from akeneo.models.asset_family_list import AssetFamilyList
from akeneo.models.asset_family_list_all_of import AssetFamilyListAllOf
from akeneo.models.asset_family_list_all_of_assign_assets_to import AssetFamilyListAllOfAssignAssetsTo
from akeneo.models.asset_family_list_all_of_labels import AssetFamilyListAllOfLabels
from akeneo.models.asset_family_list_all_of_naming_convention import AssetFamilyListAllOfNamingConvention
from akeneo.models.asset_family_list_all_of_operations import AssetFamilyListAllOfOperations
from akeneo.models.asset_family_list_all_of_operations_parameters import AssetFamilyListAllOfOperationsParameters
from akeneo.models.asset_family_list_all_of_product_link_rules import AssetFamilyListAllOfProductLinkRules
from akeneo.models.asset_family_list_all_of_product_selections import AssetFamilyListAllOfProductSelections
from akeneo.models.asset_family_list_all_of_source import AssetFamilyListAllOfSource
from akeneo.models.asset_family_list_all_of_target import AssetFamilyListAllOfTarget
from akeneo.models.asset_family_list_all_of_transformations import AssetFamilyListAllOfTransformations
from akeneo.models.asset_item_list import AssetItemList
from akeneo.models.asset_list import AssetList
from akeneo.models.asset_list_all_of import AssetListAllOf
from akeneo.models.association_type import AssociationType
from akeneo.models.association_type_list import AssociationTypeList
from akeneo.models.association_type_list_all_of import AssociationTypeListAllOf
from akeneo.models.association_type_list_all_of_labels import AssociationTypeListAllOfLabels
from akeneo.models.association_types import AssociationTypes
from akeneo.models.association_types_embedded import AssociationTypesEmbedded
from akeneo.models.association_types_embedded_items_inner import AssociationTypesEmbeddedItemsInner
from akeneo.models.association_types_embedded_items_inner_all_of import AssociationTypesEmbeddedItemsInnerAllOf
from akeneo.models.association_types_embedded_items_inner_all_of_labels import AssociationTypesEmbeddedItemsInnerAllOfLabels
from akeneo.models.attribute import Attribute
from akeneo.models.attribute_group import AttributeGroup
from akeneo.models.attribute_group_list import AttributeGroupList
from akeneo.models.attribute_group_list_all_of import AttributeGroupListAllOf
from akeneo.models.attribute_group_list_all_of_labels import AttributeGroupListAllOfLabels
from akeneo.models.attribute_groups import AttributeGroups
from akeneo.models.attribute_groups_embedded import AttributeGroupsEmbedded
from akeneo.models.attribute_groups_embedded_items_inner import AttributeGroupsEmbeddedItemsInner
from akeneo.models.attribute_groups_embedded_items_inner_all_of import AttributeGroupsEmbeddedItemsInnerAllOf
from akeneo.models.attribute_groups_embedded_items_inner_all_of_labels import AttributeGroupsEmbeddedItemsInnerAllOfLabels
from akeneo.models.attribute_list import AttributeList
from akeneo.models.attribute_list_all_of import AttributeListAllOf
from akeneo.models.attribute_list_all_of_group_labels import AttributeListAllOfGroupLabels
from akeneo.models.attribute_list_all_of_labels import AttributeListAllOfLabels
from akeneo.models.attribute_list_all_of_table_configuration import AttributeListAllOfTableConfiguration
from akeneo.models.attribute_list_all_of_validations import AttributeListAllOfValidations
from akeneo.models.attribute_option import AttributeOption
from akeneo.models.attribute_option_list import AttributeOptionList
from akeneo.models.attribute_option_list_all_of import AttributeOptionListAllOf
from akeneo.models.attribute_option_list_all_of_labels import AttributeOptionListAllOfLabels
from akeneo.models.attribute_options import AttributeOptions
from akeneo.models.attribute_options_embedded import AttributeOptionsEmbedded
from akeneo.models.attribute_options_embedded_items_inner import AttributeOptionsEmbeddedItemsInner
from akeneo.models.attribute_options_embedded_items_inner_all_of import AttributeOptionsEmbeddedItemsInnerAllOf
from akeneo.models.attribute_options_embedded_items_inner_all_of_labels import AttributeOptionsEmbeddedItemsInnerAllOfLabels
from akeneo.models.attributes import Attributes
from akeneo.models.attributes_embedded import AttributesEmbedded
from akeneo.models.attributes_embedded_items_inner import AttributesEmbeddedItemsInner
from akeneo.models.attributes_embedded_items_inner_all_of import AttributesEmbeddedItemsInnerAllOf
from akeneo.models.attributes_embedded_items_inner_all_of_group_labels import AttributesEmbeddedItemsInnerAllOfGroupLabels
from akeneo.models.attributes_embedded_items_inner_all_of_table_configuration_inner import AttributesEmbeddedItemsInnerAllOfTableConfigurationInner
from akeneo.models.attributes_embedded_items_inner_all_of_table_configuration_inner_labels import AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerLabels
from akeneo.models.attributes_embedded_items_inner_all_of_table_configuration_inner_validations import AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations
from akeneo.models.catalogs import Catalogs
from akeneo.models.catalogs_embedded import CatalogsEmbedded
from akeneo.models.catalogs_embedded_items_inner import CatalogsEmbeddedItemsInner
from akeneo.models.catalogs_embedded_items_inner_all_of import CatalogsEmbeddedItemsInnerAllOf
from akeneo.models.categories import Categories
from akeneo.models.categories_embedded import CategoriesEmbedded
from akeneo.models.categories_embedded_items_inner import CategoriesEmbeddedItemsInner
from akeneo.models.categories_embedded_items_inner_all_of import CategoriesEmbeddedItemsInnerAllOf
from akeneo.models.categories_embedded_items_inner_all_of_values import CategoriesEmbeddedItemsInnerAllOfValues
from akeneo.models.categories_embedded_items_inner_all_of_values_additional_properties_attribute_uuid_channel_code_locale_code_inner import CategoriesEmbeddedItemsInnerAllOfValuesAdditionalPropertiesAttributeUuidChannelCodeLocaleCodeInner
from akeneo.models.category import Category
from akeneo.models.category_list import CategoryList
from akeneo.models.category_list_all_of import CategoryListAllOf
from akeneo.models.category_list_all_of_values import CategoryListAllOfValues
from akeneo.models.category_list_all_of_values_additional_properties_attribute_uuid_channel_code_locale_code import CategoryListAllOfValuesAdditionalPropertiesAttributeUuidChannelCodeLocaleCode
from akeneo.models.channel import Channel
from akeneo.models.channel_list import ChannelList
from akeneo.models.channel_list_all_of import ChannelListAllOf
from akeneo.models.channel_list_all_of_conversion_units import ChannelListAllOfConversionUnits
from akeneo.models.channel_list_all_of_labels import ChannelListAllOfLabels
from akeneo.models.channels import Channels
from akeneo.models.channels_embedded import ChannelsEmbedded
from akeneo.models.channels_embedded_items_inner import ChannelsEmbeddedItemsInner
from akeneo.models.channels_embedded_items_inner_all_of import ChannelsEmbeddedItemsInnerAllOf
from akeneo.models.channels_embedded_items_inner_all_of_conversion_units import ChannelsEmbeddedItemsInnerAllOfConversionUnits
from akeneo.models.channels_embedded_items_inner_all_of_labels import ChannelsEmbeddedItemsInnerAllOfLabels
from akeneo.models.currencies import Currencies
from akeneo.models.currencies_embedded import CurrenciesEmbedded
from akeneo.models.currencies_embedded_items_inner import CurrenciesEmbeddedItemsInner
from akeneo.models.currencies_embedded_items_inner_all_of import CurrenciesEmbeddedItemsInnerAllOf
from akeneo.models.currency import Currency
from akeneo.models.currency_list import CurrencyList
from akeneo.models.currency_list_all_of import CurrencyListAllOf
from akeneo.models.deprecated_asset import DeprecatedAsset
from akeneo.models.deprecated_asset_category import DeprecatedAssetCategory
from akeneo.models.deprecated_asset_category_list import DeprecatedAssetCategoryList
from akeneo.models.deprecated_asset_category_list_all_of import DeprecatedAssetCategoryListAllOf
from akeneo.models.deprecated_asset_category_list_all_of_labels import DeprecatedAssetCategoryListAllOfLabels
from akeneo.models.deprecated_asset_list import DeprecatedAssetList
from akeneo.models.deprecated_asset_list_all_of import DeprecatedAssetListAllOf
from akeneo.models.deprecated_asset_list_all_of_link import DeprecatedAssetListAllOfLink
from akeneo.models.deprecated_asset_list_all_of_link1 import DeprecatedAssetListAllOfLink1
from akeneo.models.deprecated_asset_list_all_of_link1_download import DeprecatedAssetListAllOfLink1Download
from akeneo.models.deprecated_asset_list_all_of_link1_self import DeprecatedAssetListAllOfLink1Self
from akeneo.models.deprecated_asset_list_all_of_link_download import DeprecatedAssetListAllOfLinkDownload
from akeneo.models.deprecated_asset_list_all_of_link_self import DeprecatedAssetListAllOfLinkSelf
from akeneo.models.deprecated_asset_list_all_of_reference_files import DeprecatedAssetListAllOfReferenceFiles
from akeneo.models.deprecated_asset_list_all_of_variation_files import DeprecatedAssetListAllOfVariationFiles
from akeneo.models.deprecated_asset_reference_file import DeprecatedAssetReferenceFile
from akeneo.models.deprecated_asset_reference_file_upload_warning import DeprecatedAssetReferenceFileUploadWarning
from akeneo.models.deprecated_asset_tag import DeprecatedAssetTag
from akeneo.models.deprecated_asset_tag_list import DeprecatedAssetTagList
from akeneo.models.deprecated_asset_tag_list_all_of import DeprecatedAssetTagListAllOf
from akeneo.models.deprecated_asset_variation_file import DeprecatedAssetVariationFile
from akeneo.models.error import Error
from akeneo.models.error_by_line import ErrorByLine
from akeneo.models.error_by_line_product_uuid import ErrorByLineProductUuid
from akeneo.models.families import Families
from akeneo.models.families_embedded import FamiliesEmbedded
from akeneo.models.families_embedded_items_inner import FamiliesEmbeddedItemsInner
from akeneo.models.families_embedded_items_inner_all_of import FamiliesEmbeddedItemsInnerAllOf
from akeneo.models.families_embedded_items_inner_all_of_attribute_requirements import FamiliesEmbeddedItemsInnerAllOfAttributeRequirements
from akeneo.models.families_embedded_items_inner_all_of_labels import FamiliesEmbeddedItemsInnerAllOfLabels
from akeneo.models.family import Family
from akeneo.models.family_list import FamilyList
from akeneo.models.family_list_all_of import FamilyListAllOf
from akeneo.models.family_list_all_of_attribute_requirements import FamilyListAllOfAttributeRequirements
from akeneo.models.family_list_all_of_labels import FamilyListAllOfLabels
from akeneo.models.family_variant import FamilyVariant
from akeneo.models.family_variant_list import FamilyVariantList
from akeneo.models.family_variant_list_all_of import FamilyVariantListAllOf
from akeneo.models.family_variant_list_all_of_labels import FamilyVariantListAllOfLabels
from akeneo.models.family_variant_list_all_of_variant_attribute_sets import FamilyVariantListAllOfVariantAttributeSets
from akeneo.models.family_variants import FamilyVariants
from akeneo.models.family_variants_embedded import FamilyVariantsEmbedded
from akeneo.models.family_variants_embedded_items_inner import FamilyVariantsEmbeddedItemsInner
from akeneo.models.family_variants_embedded_items_inner_all_of import FamilyVariantsEmbeddedItemsInnerAllOf
from akeneo.models.family_variants_embedded_items_inner_all_of_labels import FamilyVariantsEmbeddedItemsInnerAllOfLabels
from akeneo.models.family_variants_embedded_items_inner_all_of_variant_attribute_sets_inner import FamilyVariantsEmbeddedItemsInnerAllOfVariantAttributeSetsInner
from akeneo.models.get_asset_families_code_attributes200_response_inner import GetAssetFamiliesCodeAttributes200ResponseInner
from akeneo.models.get_asset_family_attributes_attribute_code_options200_response_inner import GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner
from akeneo.models.get_endpoints200_response import GetEndpoints200Response
from akeneo.models.get_media_files_code200_response import GetMediaFilesCode200Response
from akeneo.models.get_media_files_code200_response_links import GetMediaFilesCode200ResponseLinks
from akeneo.models.get_products401_response import GetProducts401Response
from akeneo.models.get_reference_entities_code200_response import GetReferenceEntitiesCode200Response
from akeneo.models.get_reference_entities_code200_response_links import GetReferenceEntitiesCode200ResponseLinks
from akeneo.models.get_reference_entities_code_attributes200_response_inner import GetReferenceEntitiesCodeAttributes200ResponseInner
from akeneo.models.get_reference_entity_attributes_attribute_code_options200_response_inner import GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner
from akeneo.models.get_reference_entity_attributes_code200_response import GetReferenceEntityAttributesCode200Response
from akeneo.models.get_reference_files_locale_code200_response import GetReferenceFilesLocaleCode200Response
from akeneo.models.get_reference_files_locale_code200_response_link import GetReferenceFilesLocaleCode200ResponseLink
from akeneo.models.get_system_information200_response import GetSystemInformation200Response
from akeneo.models.get_variation_files_channel_code_locale_code200_response import GetVariationFilesChannelCodeLocaleCode200Response
from akeneo.models.get_variation_files_channel_code_locale_code200_response_link import GetVariationFilesChannelCodeLocaleCode200ResponseLink
from akeneo.models.item_list import ItemList
from akeneo.models.locale import Locale
from akeneo.models.locale_list import LocaleList
from akeneo.models.locale_list_all_of import LocaleListAllOf
from akeneo.models.locales import Locales
from akeneo.models.locales_embedded import LocalesEmbedded
from akeneo.models.locales_embedded_items_inner import LocalesEmbeddedItemsInner
from akeneo.models.locales_embedded_items_inner_all_of import LocalesEmbeddedItemsInnerAllOf
from akeneo.models.measure_families import MeasureFamilies
from akeneo.models.measure_families_embedded import MeasureFamiliesEmbedded
from akeneo.models.measure_families_embedded_items_inner import MeasureFamiliesEmbeddedItemsInner
from akeneo.models.measure_families_embedded_items_inner_all_of import MeasureFamiliesEmbeddedItemsInnerAllOf
from akeneo.models.measure_families_embedded_items_inner_all_of_units_inner import MeasureFamiliesEmbeddedItemsInnerAllOfUnitsInner
from akeneo.models.measure_family import MeasureFamily
from akeneo.models.measure_family_list import MeasureFamilyList
from akeneo.models.measure_family_list_all_of import MeasureFamilyListAllOf
from akeneo.models.measure_family_list_all_of_units import MeasureFamilyListAllOfUnits
from akeneo.models.measurement_families_get_list200_response import MeasurementFamiliesGetList200Response
from akeneo.models.measurement_families_get_list200_response_labels import MeasurementFamiliesGetList200ResponseLabels
from akeneo.models.measurement_families_get_list200_response_units import MeasurementFamiliesGetList200ResponseUnits
from akeneo.models.measurement_families_get_list200_response_units_unit_code import MeasurementFamiliesGetList200ResponseUnitsUnitCode
from akeneo.models.measurement_families_get_list200_response_units_unit_code_convert_from_standard_inner import MeasurementFamiliesGetList200ResponseUnitsUnitCodeConvertFromStandardInner
from akeneo.models.measurement_families_get_list200_response_units_unit_code_labels import MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels
from akeneo.models.measurement_family import MeasurementFamily
from akeneo.models.measurement_family_list import MeasurementFamilyList
from akeneo.models.media_file import MediaFile
from akeneo.models.media_file_all_of import MediaFileAllOf
from akeneo.models.media_file_all_of1 import MediaFileAllOf1
from akeneo.models.media_file_all_of_links import MediaFileAllOfLinks
from akeneo.models.media_file_all_of_links_download import MediaFileAllOfLinksDownload
from akeneo.models.media_file_item_list import MediaFileItemList
from akeneo.models.media_file_list import MediaFileList
from akeneo.models.media_file_list_all_of import MediaFileListAllOf
from akeneo.models.media_file_list_all_of_links import MediaFileListAllOfLinks
from akeneo.models.media_file_list_all_of_links_self import MediaFileListAllOfLinksSelf
from akeneo.models.media_files import MediaFiles
from akeneo.models.media_files_embedded import MediaFilesEmbedded
from akeneo.models.media_files_embedded_items_inner import MediaFilesEmbeddedItemsInner
from akeneo.models.media_files_embedded_items_inner_all_of import MediaFilesEmbeddedItemsInnerAllOf
from akeneo.models.media_files_embedded_items_inner_all_of1 import MediaFilesEmbeddedItemsInnerAllOf1
from akeneo.models.media_files_embedded_items_inner_all_of_links import MediaFilesEmbeddedItemsInnerAllOfLinks
from akeneo.models.media_files_embedded_items_inner_all_of_links_download import MediaFilesEmbeddedItemsInnerAllOfLinksDownload
from akeneo.models.media_files_embedded_items_inner_all_of_links_self import MediaFilesEmbeddedItemsInnerAllOfLinksSelf
from akeneo.models.pam_asset_categories import PAMAssetCategories
from akeneo.models.pam_asset_categories_embedded import PAMAssetCategoriesEmbedded
from akeneo.models.pam_asset_categories_embedded_items_inner import PAMAssetCategoriesEmbeddedItemsInner
from akeneo.models.pam_asset_categories_embedded_items_inner_all_of import PAMAssetCategoriesEmbeddedItemsInnerAllOf
from akeneo.models.pam_asset_categories_embedded_items_inner_all_of_labels import PAMAssetCategoriesEmbeddedItemsInnerAllOfLabels
from akeneo.models.pam_asset_tags import PAMAssetTags
from akeneo.models.pam_asset_tags_embedded import PAMAssetTagsEmbedded
from akeneo.models.pam_asset_tags_embedded_items_inner import PAMAssetTagsEmbeddedItemsInner
from akeneo.models.pam_asset_tags_embedded_items_inner_all_of import PAMAssetTagsEmbeddedItemsInnerAllOf
from akeneo.models.pam_assets import PAMAssets
from akeneo.models.pam_assets_embedded import PAMAssetsEmbedded
from akeneo.models.pam_assets_embedded_items_inner import PAMAssetsEmbeddedItemsInner
from akeneo.models.pam_assets_embedded_items_inner_all_of import PAMAssetsEmbeddedItemsInnerAllOf
from akeneo.models.pam_assets_embedded_items_inner_all_of_reference_files_inner import PAMAssetsEmbeddedItemsInnerAllOfReferenceFilesInner
from akeneo.models.pam_assets_embedded_items_inner_all_of_reference_files_inner_link import PAMAssetsEmbeddedItemsInnerAllOfReferenceFilesInnerLink
from akeneo.models.pam_assets_embedded_items_inner_all_of_reference_files_inner_link_download import PAMAssetsEmbeddedItemsInnerAllOfReferenceFilesInnerLinkDownload
from akeneo.models.pam_assets_embedded_items_inner_all_of_reference_files_inner_link_self import PAMAssetsEmbeddedItemsInnerAllOfReferenceFilesInnerLinkSelf
from akeneo.models.pam_assets_embedded_items_inner_all_of_variation_files_inner import PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInner
from akeneo.models.pam_assets_embedded_items_inner_all_of_variation_files_inner_link import PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLink
from akeneo.models.pam_assets_embedded_items_inner_all_of_variation_files_inner_link_download import PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload
from akeneo.models.pam_assets_embedded_items_inner_all_of_variation_files_inner_link_self import PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkSelf
from akeneo.models.pagination import Pagination
from akeneo.models.patch_asset_categories_request import PatchAssetCategoriesRequest
from akeneo.models.patch_assets_request_inner import PatchAssetsRequestInner
from akeneo.models.patch_attributes_attribute_code_options_request import PatchAttributesAttributeCodeOptionsRequest
from akeneo.models.patch_attributes_request import PatchAttributesRequest
from akeneo.models.patch_categories_request import PatchCategoriesRequest
from akeneo.models.patch_families_family_code_variants_request import PatchFamiliesFamilyCodeVariantsRequest
from akeneo.models.patch_families_request import PatchFamiliesRequest
from akeneo.models.patch_measurement_families200_response_inner import PatchMeasurementFamilies200ResponseInner
from akeneo.models.patch_measurement_families200_response_inner_errors_inner import PatchMeasurementFamilies200ResponseInnerErrorsInner
from akeneo.models.patch_pam_assets_request import PatchPamAssetsRequest
from akeneo.models.patch_product_models_request import PatchProductModelsRequest
from akeneo.models.patch_products200_response import PatchProducts200Response
from akeneo.models.patch_products_request import PatchProductsRequest
from akeneo.models.patch_products_uuid200_response import PatchProductsUuid200Response
from akeneo.models.patch_products_uuid_request import PatchProductsUuidRequest
from akeneo.models.patch_reference_entity_records200_response_inner import PatchReferenceEntityRecords200ResponseInner
from akeneo.models.patch_reference_entity_records_code_request import PatchReferenceEntityRecordsCodeRequest
from akeneo.models.patch_reference_entity_records_request_inner import PatchReferenceEntityRecordsRequestInner
from akeneo.models.post_app_catalog_request import PostAppCatalogRequest
from akeneo.models.post_media_files_request import PostMediaFilesRequest
from akeneo.models.post_products_request import PostProductsRequest
from akeneo.models.post_products_request_associations import PostProductsRequestAssociations
from akeneo.models.post_reference_entity_media_files_request import PostReferenceEntityMediaFilesRequest
from akeneo.models.post_reference_files_locale_code201_response import PostReferenceFilesLocaleCode201Response
from akeneo.models.post_reference_files_locale_code201_response_errors_inner import PostReferenceFilesLocaleCode201ResponseErrorsInner
from akeneo.models.post_reference_files_locale_code_request import PostReferenceFilesLocaleCodeRequest
from akeneo.models.post_token200_response import PostToken200Response
from akeneo.models.post_token_request import PostTokenRequest
from akeneo.models.product import Product
from akeneo.models.product_list import ProductList
from akeneo.models.product_list_all_of import ProductListAllOf
from akeneo.models.product_list_all_of1 import ProductListAllOf1
from akeneo.models.product_list_all_of1_associations import ProductListAllOf1Associations
from akeneo.models.product_list_all_of1_associations_association_type_code import ProductListAllOf1AssociationsAssociationTypeCode
from akeneo.models.product_list_all_of1_completenesses import ProductListAllOf1Completenesses
from akeneo.models.product_list_all_of1_metadata import ProductListAllOf1Metadata
from akeneo.models.product_list_all_of1_quantified_associations import ProductListAllOf1QuantifiedAssociations
from akeneo.models.product_list_all_of1_quantified_associations_quantified_association_type_code import ProductListAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCode
from akeneo.models.product_list_all_of1_quantified_associations_quantified_association_type_code_product_models import ProductListAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModels
from akeneo.models.product_list_all_of1_quantified_associations_quantified_association_type_code_products import ProductListAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProducts
from akeneo.models.product_list_all_of_links import ProductListAllOfLinks
from akeneo.models.product_list_all_of_links_self import ProductListAllOfLinksSelf
from akeneo.models.product_model import ProductModel
from akeneo.models.product_model_list import ProductModelList
from akeneo.models.product_model_list_all_of import ProductModelListAllOf
from akeneo.models.product_model_list_all_of_associations import ProductModelListAllOfAssociations
from akeneo.models.product_model_list_all_of_metadata import ProductModelListAllOfMetadata
from akeneo.models.product_model_list_all_of_quantified_associations import ProductModelListAllOfQuantifiedAssociations
from akeneo.models.product_model_list_all_of_quantified_associations_quantified_association_type_code import ProductModelListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
from akeneo.models.product_models import ProductModels
from akeneo.models.product_models_embedded import ProductModelsEmbedded
from akeneo.models.product_models_embedded_items_inner import ProductModelsEmbeddedItemsInner
from akeneo.models.product_models_embedded_items_inner_all_of import ProductModelsEmbeddedItemsInnerAllOf
from akeneo.models.product_models_embedded_items_inner_all_of_associations import ProductModelsEmbeddedItemsInnerAllOfAssociations
from akeneo.models.product_models_embedded_items_inner_all_of_metadata import ProductModelsEmbeddedItemsInnerAllOfMetadata
from akeneo.models.product_models_embedded_items_inner_all_of_quantified_associations import ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociations
from akeneo.models.product_models_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
from akeneo.models.product_models_embedded_items_inner_all_of_values_value_inner import ProductModelsEmbeddedItemsInnerAllOfValuesValueInner
from akeneo.models.product_uuid import ProductUuid
from akeneo.models.product_uuid_associations import ProductUuidAssociations
from akeneo.models.product_uuid_associations_association_type_code import ProductUuidAssociationsAssociationTypeCode
from akeneo.models.product_uuid_list import ProductUuidList
from akeneo.models.product_uuid_list_all_of import ProductUuidListAllOf
from akeneo.models.product_uuid_list_all_of_associations import ProductUuidListAllOfAssociations
from akeneo.models.product_uuid_list_all_of_quantified_associations import ProductUuidListAllOfQuantifiedAssociations
from akeneo.models.product_uuid_list_all_of_quantified_associations_quantified_association_type_code import ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
from akeneo.models.product_uuid_list_all_of_quantified_associations_quantified_association_type_code_products import ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts
from akeneo.models.product_uuids import ProductUuids
from akeneo.models.product_uuids_embedded import ProductUuidsEmbedded
from akeneo.models.products import Products
from akeneo.models.products1 import Products1
from akeneo.models.products1_embedded import Products1Embedded
from akeneo.models.products1_embedded_items_inner import Products1EmbeddedItemsInner
from akeneo.models.products1_embedded_items_inner_all_of import Products1EmbeddedItemsInnerAllOf
from akeneo.models.products1_embedded_items_inner_all_of_associations import Products1EmbeddedItemsInnerAllOfAssociations
from akeneo.models.products1_embedded_items_inner_all_of_quantified_associations import Products1EmbeddedItemsInnerAllOfQuantifiedAssociations
from akeneo.models.products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
from akeneo.models.products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_products_inner import Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner
from akeneo.models.products2 import Products2
from akeneo.models.products_embedded import ProductsEmbedded
from akeneo.models.products_embedded_items_inner import ProductsEmbeddedItemsInner
from akeneo.models.products_embedded_items_inner_all_of import ProductsEmbeddedItemsInnerAllOf
from akeneo.models.products_embedded_items_inner_all_of1 import ProductsEmbeddedItemsInnerAllOf1
from akeneo.models.products_embedded_items_inner_all_of1_associations_value import ProductsEmbeddedItemsInnerAllOf1AssociationsValue
from akeneo.models.products_embedded_items_inner_all_of1_completenesses_inner import ProductsEmbeddedItemsInnerAllOf1CompletenessesInner
from akeneo.models.products_embedded_items_inner_all_of1_metadata import ProductsEmbeddedItemsInnerAllOf1Metadata
from akeneo.models.products_embedded_items_inner_all_of1_quantified_associations import ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociations
from akeneo.models.products_embedded_items_inner_all_of1_quantified_associations_quantified_association_type_code import ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCode
from akeneo.models.products_embedded_items_inner_all_of1_quantified_associations_quantified_association_type_code_product_models_inner import ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner
from akeneo.models.products_embedded_items_inner_all_of1_quantified_associations_quantified_association_type_code_products_inner import ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner
from akeneo.models.products_embedded_items_inner_all_of1_values_value_inner import ProductsEmbeddedItemsInnerAllOf1ValuesValueInner
from akeneo.models.products_embedded_items_inner_all_of1_values_value_inner_linked_data import ProductsEmbeddedItemsInnerAllOf1ValuesValueInnerLinkedData
from akeneo.models.products_embedded_items_inner_all_of_links import ProductsEmbeddedItemsInnerAllOfLinks
from akeneo.models.products_embedded_items_inner_all_of_links_self import ProductsEmbeddedItemsInnerAllOfLinksSelf
from akeneo.models.products_links import ProductsLinks
from akeneo.models.products_links_first import ProductsLinksFirst
from akeneo.models.products_links_next import ProductsLinksNext
from akeneo.models.products_links_previous import ProductsLinksPrevious
from akeneo.models.products_links_self import ProductsLinksSelf
from akeneo.models.published_product import PublishedProduct
from akeneo.models.published_product_list import PublishedProductList
from akeneo.models.published_product_list_all_of import PublishedProductListAllOf
from akeneo.models.published_product_list_all_of_associations import PublishedProductListAllOfAssociations
from akeneo.models.published_products import PublishedProducts
from akeneo.models.published_products_embedded import PublishedProductsEmbedded
from akeneo.models.published_products_embedded_items_inner import PublishedProductsEmbeddedItemsInner
from akeneo.models.published_products_embedded_items_inner_all_of import PublishedProductsEmbeddedItemsInnerAllOf
from akeneo.models.published_products_embedded_items_inner_all_of_associations import PublishedProductsEmbeddedItemsInnerAllOfAssociations
from akeneo.models.reference_entities import ReferenceEntities
from akeneo.models.reference_entities_embedded import ReferenceEntitiesEmbedded
from akeneo.models.reference_entities_embedded_items_inner import ReferenceEntitiesEmbeddedItemsInner
from akeneo.models.reference_entities_embedded_items_inner_all_of import ReferenceEntitiesEmbeddedItemsInnerAllOf
from akeneo.models.reference_entities_embedded_items_inner_all_of1 import ReferenceEntitiesEmbeddedItemsInnerAllOf1
from akeneo.models.reference_entities_embedded_items_inner_all_of1_labels import ReferenceEntitiesEmbeddedItemsInnerAllOf1Labels
from akeneo.models.reference_entities_embedded_items_inner_all_of_links import ReferenceEntitiesEmbeddedItemsInnerAllOfLinks
from akeneo.models.reference_entities_embedded_items_inner_all_of_links_image_download import ReferenceEntitiesEmbeddedItemsInnerAllOfLinksImageDownload
from akeneo.models.reference_entities_links import ReferenceEntitiesLinks
from akeneo.models.reference_entity import ReferenceEntity
from akeneo.models.reference_entity_all_of import ReferenceEntityAllOf
from akeneo.models.reference_entity_all_of1 import ReferenceEntityAllOf1
from akeneo.models.reference_entity_all_of1_labels import ReferenceEntityAllOf1Labels
from akeneo.models.reference_entity_all_of_links import ReferenceEntityAllOfLinks
from akeneo.models.reference_entity_all_of_links_image_download import ReferenceEntityAllOfLinksImageDownload
from akeneo.models.reference_entity_attribute import ReferenceEntityAttribute
from akeneo.models.reference_entity_attribute_option import ReferenceEntityAttributeOption
from akeneo.models.reference_entity_item_list import ReferenceEntityItemList
from akeneo.models.reference_entity_list import ReferenceEntityList
from akeneo.models.reference_entity_list_all_of import ReferenceEntityListAllOf
from akeneo.models.reference_entity_list_all_of_links import ReferenceEntityListAllOfLinks
from akeneo.models.reference_entity_record import ReferenceEntityRecord
from akeneo.models.reference_entity_record_embedded import ReferenceEntityRecordEmbedded
from akeneo.models.reference_entity_record_embedded_items_inner import ReferenceEntityRecordEmbeddedItemsInner
from akeneo.models.reference_entity_record_embedded_items_inner_all_of import ReferenceEntityRecordEmbeddedItemsInnerAllOf
from akeneo.models.reference_entity_record_embedded_items_inner_all_of_values_value_inner import ReferenceEntityRecordEmbeddedItemsInnerAllOfValuesValueInner
from akeneo.models.reference_entity_record_item_list import ReferenceEntityRecordItemList
from akeneo.models.reference_entity_record_list import ReferenceEntityRecordList
from akeneo.models.reference_entity_record_list_all_of import ReferenceEntityRecordListAllOf
from akeneo.models.search_after_pagination import SearchAfterPagination
from akeneo.models.several_association_types_patch_request import SeveralAssociationTypesPatchRequest
from akeneo.models.several_attribute_groups_patch_request import SeveralAttributeGroupsPatchRequest
from akeneo.models.several_channels_patch_request import SeveralChannelsPatchRequest
