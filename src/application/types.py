from enum import Enum


class StatusType(Enum):
    NOT_STARTED = "not_started"
    PENDING = "pending"
    PARSING = "parsing"
    SAVING = "saving"
    DONE = "done"
    ERROR = "error"
