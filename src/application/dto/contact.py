from dataclasses import dataclass, field

from .base import BaseData


@dataclass(slots=True)
class ContactData(BaseData):
    website: str
    id: int | None = None
    emails: list[str] = field(default_factory=list)
    phones: list[str] = field(default_factory=list)


@dataclass(slots=True)
class UpdateContactData(BaseData):
    emails: list[str] | None = None
    phones: list[str] | None = None
