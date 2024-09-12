from dataclasses import dataclass

from application.types import StatusType

from .base import BaseData


@dataclass(slots=True)
class UploadFile(BaseData):
    filename: str
    id: int | None = None


@dataclass(slots=True, init=False)
class Upload(BaseData):
    id: int | None = None
    uuid_id: str | None = None
    file_id: int | None = None

    _urls: list[str] | None = None
    status: StatusType = StatusType.NOT_STARTED

    def __init__(
            self,
            urls: list[str] | str | None = None,
            status: StatusType = StatusType.NOT_STARTED,
            id: int | None = None,
            uuid_id: str | None = None,
            file_id: int | None = None,
    ):
        self.urls: list[str] | str = urls
        self.status: StatusType = status
        self.id: int | None = id,
        self.uuid_id: str | None = uuid_id,
        self.file_id: int | None = file_id,

    @property
    def urls(self) -> list[str]:
        return self._urls

    @urls.setter
    def urls(self, urls: list[str] | str):
        if isinstance(urls, str):
            urls = [url for url in urls.split(",")] if urls else []

        self._urls = urls

    def urls_to_str(self) -> str:
        return ",".join(self._urls)
