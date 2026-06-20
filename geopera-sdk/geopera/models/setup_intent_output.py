from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetupIntentOutput")


@_attrs_define
class SetupIntentOutput:
    """
    Attributes:
        client_secret (str):
        setup_intent_id (str):
        customer_id (str):
        env (str):
    """

    client_secret: str
    setup_intent_id: str
    customer_id: str
    env: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_secret = self.client_secret

        setup_intent_id = self.setup_intent_id

        customer_id = self.customer_id

        env = self.env

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_secret": client_secret,
                "setup_intent_id": setup_intent_id,
                "customer_id": customer_id,
                "env": env,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_secret = d.pop("client_secret")

        setup_intent_id = d.pop("setup_intent_id")

        customer_id = d.pop("customer_id")

        env = d.pop("env")

        setup_intent_output = cls(
            client_secret=client_secret,
            setup_intent_id=setup_intent_id,
            customer_id=customer_id,
            env=env,
        )

        setup_intent_output.additional_properties = d
        return setup_intent_output

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
