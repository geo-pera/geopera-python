from enum import Enum


class VisualizationSpecKind(str, Enum):
    ELEVATION = "elevation"
    INDEX = "index"
    RAW = "raw"
    RGB = "rgb"

    def __str__(self) -> str:
        return str(self.value)
