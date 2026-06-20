from enum import Enum


class ItemType(str, Enum):
    CLIP = "clip"
    DERIVED_RASTER = "derived_raster"
    DERIVED_VECTOR = "derived_vector"
    EXTERNAL_REFERENCE = "external_reference"
    SATELLITE_CAPTURE = "satellite_capture"
    USER_RASTER = "user_raster"
    USER_VECTOR = "user_vector"

    def __str__(self) -> str:
        return str(self.value)
