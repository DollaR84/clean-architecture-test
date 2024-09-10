from dataclasses import dataclass, field

from .base import BaseData


@dataclass(slots=True)
class UploadData(BaseData):
    urls: list[str] = field(default_factory=list)


@dataclass(slots=True)
class UploadFile(BaseData):
    id: int | None = None
    filename: str


class UploadCsvFile(UploadFile):
    pass


class UploadTxtFile(UploadFile):
    pass
