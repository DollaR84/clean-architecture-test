from dataclasses import dataclass, field

from application.types import StatusType

from .base import BaseData


@dataclass(slots=True)
class UploadData(BaseData):
    urls: list[str] = field(default_factory=list)


@dataclass(slots=True)
class UploadFile(BaseData):
    filename: str
    id: int | None = None


class UploadCsvFile(UploadFile):
    pass


class UploadTxtFile(UploadFile):
    pass


@dataclass(slots=True)
class Upload(BaseData):
    id: int | None = None
    uuid_id: str | None = None
    file_id: int | None = None

    urls: list[str] | None = None
    status: StatusType = StatusType.NOT_STARTED
