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
    ADVANCE_TIME = 8
    GENERATE_FILE = 9
    UNLOAD = 10

    DISCONNECT = 11


translate = {
    "UNRECOGNIZED": Request.UNRECOGNIZED,
    "REGISTER": Request.REGISTER,
    "START": Request.LAUNCH_DIAGNOSTIC,
    "LOAD_BATTERIES": Request.LOAD_BATTERIES,
    "ABORT_DIAGNOSTIC": Request.ABORT_DIAGNOSTIC,
    "LOAD": Request.LOAD,
    "SAVE": Request.SAVE,
    "TO_STRING": Request.TO_STRING,
    "POP": Request.POP,
    "ADVANCE_TIME": Request.ADVANCE_TIME,
    "GENERATE_FILE": Request.GENERATE_FILE,
    "UNLOAD": Request.UNLOAD,

    "DISCONNECT": Request.DISCONNECT,

    Request.UNRECOGNIZED: "UNRECOGNIZED",
    Request.REGISTER: "REGISTER",
    Request.LAUNCH_DIAGNOSTIC: "START",
    Request.LOAD_BATTERIES: "LOAD_BATTERIES",
    Request.ABORT_DIAGNOSTIC: "ABORT_DIAGNOSTIC",
    Request.LOAD: "LOAD",
    Request.SAVE: "SAVE",
    Request.TO_STRING: "TO_STRING",
    Request.POP: "POP",
    Request.ADVANCE_TIME: "ADVANCE_TIME",
    Request.GENERATE_FILE: "GENERATE_FILE",
    Request.UNLOAD: "UNLOAD",

    Request.DISCONNECT: "DISCONNECT"
}

