from enum import Enum


class Error(Enum):
    """
    Error code.
    """
    ERR_NONE = 0
    ERR_ILLEGAL_ARGUMENT = 1
    ERR_TEMP = 2
    ERR_NO_SLOTS = 3
    ERR_DIAG_TOO_EARLY = 4

    messages = ["", "Illegal Argument used", "Temperature does not match, {} instead of {}",
                "There is no slot available",
                "You ordered a diagnostic too early you have to wait until {}"]
