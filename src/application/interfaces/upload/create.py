from abc import abstractmethod
from typing import Protocol

import domain


class CreateUploadFile(Protocol):

    @abstractmethod
    async def create_upload_file(
            self,
            data: domain.UploadFile,
    ) -> domain.UploadFile:
        ...


class CreateUpload(Protocol):

    @abstractmethod
    async def create_upload(
            self,
            data: domain.Upload,
    ) -> domain.Upload:
        ...
