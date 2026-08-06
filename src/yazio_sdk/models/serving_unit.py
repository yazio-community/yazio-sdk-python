from enum import Enum


class ServingUnit(str, Enum):
    BAR = "bar"
    BOTTLE = "bottle"
    CAN = "can"
    CUP = "cup"
    EACH = "each"
    GLASS = "glass"
    PACKAGE = "package"
    PIECE = "piece"
    PORTION = "portion"
    SLICE = "slice"
    TABLESPOON = "tablespoon"
    TABLET = "tablet"
    TEASPOON = "teaspoon"

    def __str__(self) -> str:
        return str(self.value)
