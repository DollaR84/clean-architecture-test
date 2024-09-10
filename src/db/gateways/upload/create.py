import logging

import domain

from sqlalchemy.exc import SQLAlchemyError

from ..base import BaseGateway

from ...models import UploadFile


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
