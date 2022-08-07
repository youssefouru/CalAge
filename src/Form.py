from enum import Enum


class Form(Enum):
    Cylindrical = 0
    Pouch = 1
    Prismatic = 2


switcher = {
    0: Form.Cylindrical,
    1: Form.Pouch,
    2: Form.Prismatic
}

translator = {
    Form.Cylindrical: "Cylindrical",
    Form.Pouch: "Pouch",
    Form.Prismatic: "Prismatic",

    "Prismatic": Form.Prismatic,
    "Pouch": Form.Pouch,
    "Cylindrical": Form.Cylindrical
}
