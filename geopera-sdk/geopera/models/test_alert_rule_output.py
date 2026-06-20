from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TestAlertRuleOutput")


@_attrs_define
class TestAlertRuleOutput:
    """
    Attributes:
        computed_value (float):
        threshold (float):
        comparison (str):
        would_trigger (bool):
        expression (str):
        item_id (str):
    """

    computed_value: float
    threshold: float
    comparison: str
    would_trigger: bool
    expression: str
    item_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        computed_value = self.computed_value

        threshold = self.threshold

        comparison = self.comparison

        would_trigger = self.would_trigger

        expression = self.expression

        item_id = self.item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "computed_value": computed_value,
                "threshold": threshold,
                "comparison": comparison,
                "would_trigger": would_trigger,
                "expression": expression,
                "item_id": item_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        computed_value = d.pop("computed_value")

        threshold = d.pop("threshold")

        comparison = d.pop("comparison")

        would_trigger = d.pop("would_trigger")

        expression = d.pop("expression")

        item_id = d.pop("item_id")

        test_alert_rule_output = cls(
            computed_value=computed_value,
            threshold=threshold,
            comparison=comparison,
            would_trigger=would_trigger,
            expression=expression,
            item_id=item_id,
        )

        test_alert_rule_output.additional_properties = d
        return test_alert_rule_output

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
