from enum import Enum


class ProfileType(str, Enum):
    EXPRESSION = "expression"
    MULTIBAND = "multiband"
    RGB = "rgb"
    SINGLEBAND = "singleband"

    def __str__(self) -> str:
        return str(self.value)
