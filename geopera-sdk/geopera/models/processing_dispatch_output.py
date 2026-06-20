from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.processing_dispatch_output_dispatch import ProcessingDispatchOutputDispatch
    from ..models.processing_dispatch_output_job import ProcessingDispatchOutputJob


T = TypeVar("T", bound="ProcessingDispatchOutput")


@_attrs_define
class ProcessingDispatchOutput:
    """
    Attributes:
        job (ProcessingDispatchOutputJob | Unset):
        dispatch (ProcessingDispatchOutputDispatch | Unset):
    """

    job: ProcessingDispatchOutputJob | Unset = UNSET
    dispatch: ProcessingDispatchOutputDispatch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()

        dispatch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dispatch, Unset):
            dispatch = self.dispatch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job is not UNSET:
            field_dict["job"] = job
        if dispatch is not UNSET:
            field_dict["dispatch"] = dispatch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_dispatch_output_dispatch import ProcessingDispatchOutputDispatch
        from ..models.processing_dispatch_output_job import ProcessingDispatchOutputJob

        d = dict(src_dict)
        _job = d.pop("job", UNSET)
        job: ProcessingDispatchOutputJob | Unset
        if isinstance(_job, Unset):
            job = UNSET
        else:
            job = ProcessingDispatchOutputJob.from_dict(_job)

        _dispatch = d.pop("dispatch", UNSET)
        dispatch: ProcessingDispatchOutputDispatch | Unset
        if isinstance(_dispatch, Unset):
            dispatch = UNSET
        else:
            dispatch = ProcessingDispatchOutputDispatch.from_dict(_dispatch)

        processing_dispatch_output = cls(
            job=job,
            dispatch=dispatch,
        )

        processing_dispatch_output.additional_properties = d
        return processing_dispatch_output

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
