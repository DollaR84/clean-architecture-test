from pydantic import BaseModel


class UploadData(BaseModel):
    urls: list[str] = []


class UploadResponse(BaseModel):
    uuid: str
    status: str
