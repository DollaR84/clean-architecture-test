from pydantic import BaseModel


class UploadData(BaseModel):
    urls: list[str] = []
