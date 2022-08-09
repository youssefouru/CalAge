from enum import Enum


class Request(Enum):
    UNRECOGNIZED = -1
    REGISTER = 0
    LAUNCH_DIAGNOSTIC = 1
    LOAD_BATTERIES = 2
    ABORT_DIAGNOSTIC = 3
    LOAD = 4
    SAVE = 5
    TO_STRING = 6
    POP = 7

    DISCONNECT = 8


translate = {
    "UNRECOGNIZED": Request.UNRECOGNIZED,
    "REGISTER": Request.REGISTER,
    "LAUNCH_DIAGNOSTIC": Request.LAUNCH_DIAGNOSTIC,
    "LOAD_BATTERIES": Request.LOAD_BATTERIES,
    "ABORT_DIAGNOSTIC": Request.ABORT_DIAGNOSTIC,
    "LOAD": Request.LOAD,
    "SAVE": Request.SAVE,
    "TO_STRING": Request.TO_STRING,
    "POP": Request.POP,

    "DISCONNECT": Request.DISCONNECT,

    Request.UNRECOGNIZED: "UNRECOGNIZED",
    Request.REGISTER: "REGISTER",
    Request.LAUNCH_DIAGNOSTIC: "LAUNCH_DIAGNOSTIC",
    Request.LOAD_BATTERIES: "LOAD_BATTERIES",
    Request.ABORT_DIAGNOSTIC: "ABORT_DIAGNOSTIC",
    Request.LOAD: "LOAD",
    Request.SAVE: "SAVE",
    Request.TO_STRING: "TO_STRING",
    Request.POP: "POP",

    Request.DISCONNECT: "DISCONNECT"
}

