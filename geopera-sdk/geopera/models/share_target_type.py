from enum import Enum


class ShareTargetType(str, Enum):
    COLLECTION = "collection"
    ITEM = "item"

    def __str__(self) -> str:
        return str(self.value)
