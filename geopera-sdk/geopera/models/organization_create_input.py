from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_create_input_billing_address_type_0 import OrganizationCreateInputBillingAddressType0


T = TypeVar("T", bound="OrganizationCreateInput")


@_attrs_define
class OrganizationCreateInput:
    """
    Attributes:
        name (str):
        description (None | str | Unset):
        website (None | str | Unset):
        industry (None | str | Unset):
        size (None | str | Unset):
        country (None | str | Unset):
        abn (None | str | Unset):
        tax_number (None | str | Unset):
        billing_email (None | str | Unset):
        billing_admin_id (None | str | Unset):
        billing_address (None | OrganizationCreateInputBillingAddressType0 | Unset):
        enterprise_billing (bool | Unset):  Default: False.
    """

    name: str
    description: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    industry: None | str | Unset = UNSET
    size: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    abn: None | str | Unset = UNSET
    tax_number: None | str | Unset = UNSET
    billing_email: None | str | Unset = UNSET
    billing_admin_id: None | str | Unset = UNSET
    billing_address: None | OrganizationCreateInputBillingAddressType0 | Unset = UNSET
    enterprise_billing: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_create_input_billing_address_type_0 import OrganizationCreateInputBillingAddressType0

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        size: None | str | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        abn: None | str | Unset
        if isinstance(self.abn, Unset):
            abn = UNSET
        else:
            abn = self.abn

        tax_number: None | str | Unset
        if isinstance(self.tax_number, Unset):
            tax_number = UNSET
        else:
            tax_number = self.tax_number

        billing_email: None | str | Unset
        if isinstance(self.billing_email, Unset):
            billing_email = UNSET
        else:
            billing_email = self.billing_email

        billing_admin_id: None | str | Unset
        if isinstance(self.billing_admin_id, Unset):
            billing_admin_id = UNSET
        else:
            billing_admin_id = self.billing_admin_id

        billing_address: dict[str, Any] | None | Unset
        if isinstance(self.billing_address, Unset):
            billing_address = UNSET
        elif isinstance(self.billing_address, OrganizationCreateInputBillingAddressType0):
            billing_address = self.billing_address.to_dict()
        else:
            billing_address = self.billing_address

        enterprise_billing = self.enterprise_billing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if website is not UNSET:
            field_dict["website"] = website
        if industry is not UNSET:
            field_dict["industry"] = industry
        if size is not UNSET:
            field_dict["size"] = size
        if country is not UNSET:
            field_dict["country"] = country
        if abn is not UNSET:
            field_dict["abn"] = abn
        if tax_number is not UNSET:
            field_dict["tax_number"] = tax_number
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email
        if billing_admin_id is not UNSET:
            field_dict["billing_admin_id"] = billing_admin_id
        if billing_address is not UNSET:
            field_dict["billing_address"] = billing_address
        if enterprise_billing is not UNSET:
            field_dict["enterprise_billing"] = enterprise_billing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_create_input_billing_address_type_0 import OrganizationCreateInputBillingAddressType0

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_abn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abn = _parse_abn(d.pop("abn", UNSET))

        def _parse_tax_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_number = _parse_tax_number(d.pop("tax_number", UNSET))

        def _parse_billing_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_email = _parse_billing_email(d.pop("billing_email", UNSET))

        def _parse_billing_admin_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_admin_id = _parse_billing_admin_id(d.pop("billing_admin_id", UNSET))

        def _parse_billing_address(data: object) -> None | OrganizationCreateInputBillingAddressType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billing_address_type_0 = OrganizationCreateInputBillingAddressType0.from_dict(data)

                return billing_address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationCreateInputBillingAddressType0 | Unset, data)

        billing_address = _parse_billing_address(d.pop("billing_address", UNSET))

        enterprise_billing = d.pop("enterprise_billing", UNSET)

        organization_create_input = cls(
            name=name,
            description=description,
            website=website,
            industry=industry,
            size=size,
            country=country,
            abn=abn,
            tax_number=tax_number,
            billing_email=billing_email,
            billing_admin_id=billing_admin_id,
            billing_address=billing_address,
            enterprise_billing=enterprise_billing,
        )

        organization_create_input.additional_properties = d
        return organization_create_input

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
