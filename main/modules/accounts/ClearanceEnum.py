from enum import IntEnum


class ClearanceEnum(IntEnum):
    BANNED = 0
    NORMAL = 1
    ADMIN = 2
    SUPER_ADMIN = 5
