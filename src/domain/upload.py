from dataclasses import dataclass

from .base import BaseData


@dataclass(slots=True)
class UploadFile(BaseData):
    id: int | None = None
    filename: str
