import uuid

from pydantic import BaseModel


class UploadData(BaseModel):
    urls: list[str] = []


class UploadResponse(BaseModel):
    uuid: uuid.UUID
    status: str
