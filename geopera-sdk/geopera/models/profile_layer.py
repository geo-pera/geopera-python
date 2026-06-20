from enum import Enum


class ProfileLayer(str, Enum):
    AUTO = "auto"
    SENSOR = "sensor"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
