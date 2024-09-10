from pydantic import BaseModel, EmailStr


class ContactData(BaseModel):
    id: int | None = None
    website: str
    emails: list[EmailStr] = []
    phones: list[str] = []


class UpdateContactData(BaseModel):
    emails: list[EmailStr] | None = None
    phones: list[str] | None = None
