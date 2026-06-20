from enum import Enum


class LifecycleState(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"
    EXPIRED = "expired"
    EXPIRING = "expiring"

    def __str__(self) -> str:
        return str(self.value)
