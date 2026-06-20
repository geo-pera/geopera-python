from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_execute_input_inputs import ProcessExecuteInputInputs


T = TypeVar("T", bound="ProcessExecuteInput")


@_attrs_define
class ProcessExecuteInput:
    """
    Attributes:
        process_id (str):
        workspace_id (str):
        inputs (ProcessExecuteInputInputs | Unset):
    """

    process_id: str
    workspace_id: str
    inputs: ProcessExecuteInputInputs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_id = self.process_id

        workspace_id = self.workspace_id

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process_id": process_id,
                "workspaceId": workspace_id,
            }
        )
        if inputs is not UNSET:
            field_dict["inputs"] = inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_execute_input_inputs import ProcessExecuteInputInputs

        d = dict(src_dict)
        process_id = d.pop("process_id")

        workspace_id = d.pop("workspaceId")

        _inputs = d.pop("inputs", UNSET)
        inputs: ProcessExecuteInputInputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ProcessExecuteInputInputs.from_dict(_inputs)

        process_execute_input = cls(
            process_id=process_id,
            workspace_id=workspace_id,
            inputs=inputs,
        )

        process_execute_input.additional_properties = d
        return process_execute_input

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
