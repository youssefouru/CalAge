from enum import Enum


class Form(Enum):
    NONE = -1
    Cylindrical = 0
    Pouch = 1
    Prismatic = 2

    switcher = {
        0: Cylindrical,
        1: Pouch,
        2: Prismatic
    }
