from dataclasses import dataclass

from .base import BaseData


@dataclass(slots=True)
class BaseContactData(BaseData):
    _emails: list[str] | None
    _phones: list[str] | None

    @property
    def emails(self) -> list[str] | None:
        return self._emails

    @emails.setter
    def emails(self, emails: list[str] | str | None):
        if isinstance(emails, str):
            emails = [email for email in emails.split(",")] if emails else []

        self._emails = emails

    @property
    def phones(self) -> list[str] | None:
        return self._phones

    @phones.setter
    def phones(self, phones: list[str] | str | None):
        if isinstance(phones, str):
            phones = [phone for phone in phones.split(",")] if phones else []

        self._phones = phones

    def emails_to_str(self) -> str:
        return ",".join(self._emails) if self._emails is not None else self._emails

    def phones_to_str(self) -> str:
        return ",".join(self._phones) if self._phones is not None else self._phones


@dataclass(slots=True, init=False)
class ContactData(BaseContactData):
    website: str
    id: int | None

    def __init__(
            self,
            website: str,
            id: int | None = None,
            emails: list[str] | str = [],
            phones: list[str] | str = [],
    ):
        self.website: str = website
        self.id: int | None = id
        self.emails: list[str] | str = emails
        self.phones: list[str] | str = phones


@dataclass(slots=True, init=False)
class UpdateContactData(BaseContactData):

    def __init__(
            self,
            emails: list[str] | str | None = None,
            phones: list[str] | str | None = None,
    ):
        self.emails: list[str] | str | None = emails
        self.phones: list[str] | str | None = phones
