from django.db import models


class StatusType(models.TextChoices):
    NOT_STARTED = "not_started"
    PENDING = "pending"
    PARSING = "parsing"
    SAVING = "saving"
    DONE = "done"
    ERROR = "error"
