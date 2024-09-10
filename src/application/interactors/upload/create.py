from application import dto
from application import interfaces

import domain


class CreateUploadFile:

    def __init__(self, gateway: interfaces.CreateUploadFile):
        self.gateway = gateway

    async def __call__(
            self,
            data: dto.UploadFile,
    ) -> dto.UploadFile:
        data = domain.UploadFile(**data.dict())
        result = await self.gateway.create_upload_file(data)
        return dto.UploadFile(**result.dict())
