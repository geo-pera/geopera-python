from enum import Enum


class GcsRegion(str, Enum):
    ASIA_SOUTHEAST1 = "asia-southeast1"
    AUSTRALIA_SOUTHEAST1 = "australia-southeast1"
    EUROPE_WEST1 = "europe-west1"
    US_WEST1 = "us-west1"

    def __str__(self) -> str:
        return str(self.value)
