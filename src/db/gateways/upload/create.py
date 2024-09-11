import logging

import domain

from sqlalchemy.exc import SQLAlchemyError

from ..base import BaseGateway

from ...models import Upload, UploadFile


class CreateUploadFile(BaseGateway):

    async def create_upload_file(
            self,
            data: domain.UploadFile,
    ) -> domain.UploadFile:
        upload_file = UploadFile(
            filename=data.filename,
        )

        try:
            self.session.add(upload_file)
            await self.session.commit()

            data.id = upload_file.id
            return data
        except SQLAlchemyError as error:
            logging.error(error, exc_info=True)
            raise ValueError("Error creating new UploadFile record")


class CreateUpload(BaseGateway):

    async def create_upload(
            self,
            data: domain.Upload,
    ) -> domain.Upload:
        upload = Upload(
            **data.dict(exclude_unset=True, exclude=["urls"])
        )
        upload.urls = data.urls_to_str()

        try:
            self.session.add(upload)
            await self.session.commit()

            data.id = upload.id
            if data.uuid_id is None:
                data.uuid_id = upload.uuid_id
            return data
        except SQLAlchemyError as error:
            logging.error(error, exc_info=True)
            raise ValueError("Error creating new Upload record")
