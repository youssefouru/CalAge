from enum import Enum


class Request(Enum):
    UNRECOGNIZED = -1
    REGISTER_BATTERY = 0
    REGISTER_TEMPERATURE_CHAMBER = 1
    REGISTER_DIAGNOSTIC_CHAMBER = 2
    LAUNCH_DIAGNOSTIC = 3
    LOAD_BATTERIES = 4
    ABORT_DIAGNOSTIC = 5

    DISCONNECT = 6


translate = {
    "UNRECOGNIZED": Request.UNRECOGNIZED,
    "REGISTER_BATTERY": Request.REGISTER_BATTERY,
    "REGISTER_TEMPERATURE_CHAMBER": Request.REGISTER_TEMPERATURE_CHAMBER,
    "REGISTER_DIAGNOSTIC_CHAMBER": Request.REGISTER_DIAGNOSTIC_CHAMBER,
    "LAUNCH_DIAGNOSTIC": Request.LAUNCH_DIAGNOSTIC,
    "LOAD_BATTERIES": Request.LOAD_BATTERIES,
    "ABORT_DIAGNOSTIC": Request.ABORT_DIAGNOSTIC,

    "DISCONNECT": Request.DISCONNECT,

    Request.UNRECOGNIZED: "UNRECOGNIZED",
    Request.REGISTER_BATTERY: "REGISTER_BATTERY",
    Request.REGISTER_TEMPERATURE_CHAMBER: "REGISTER_TEMPERATURE_CHAMBER",
    Request.REGISTER_DIAGNOSTIC_CHAMBER: "REGISTER_DIAGNOSTIC_CHAMBER",
    Request.LAUNCH_DIAGNOSTIC: "LAUNCH_DIAGNOSTIC",
    Request.LOAD_BATTERIES: "LOAD_BATTERIES",
    Request.ABORT_DIAGNOSTIC: "ABORT_DIAGNOSTIC",

    Request.DISCONNECT: "DISCONNECT"
}

format = {
    Request.REGISTER_BATTERY: "REGISTER_BATTERY {} {} {} {} {} {} {} {}",
    Request.REGISTER_TEMPERATURE_CHAMBER: "REGISTER_TEMPERATURE_CHAMBER {}",
    Request.REGISTER_DIAGNOSTIC_CHAMBER: "REGISTER_DIAGNOSTIC_CHAMBER {} {} {}",
    Request.LAUNCH_DIAGNOSTIC: "LAUNCH_DIAGNOSTIC",
    Request.LOAD_BATTERIES: "LOAD_BATTERIES {}",
    Request.ABORT_DIAGNOSTIC: "ABORT_DIAGNOSTIC",

    Request.DISCONNECT: "DISCONNECT"
}
