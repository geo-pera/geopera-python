from enum import Enum


class SharePermission(str, Enum):
    DOWNLOAD = "download"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
