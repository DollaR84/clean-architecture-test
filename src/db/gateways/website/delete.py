import logging

from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError

from ..base import BaseGateway

from ...models import WebsiteInfo


class DeleteWebsiteInfo(BaseGateway):

    async def delete_website(
            self,
            website_id: int,
    ):
        stmt = delete(WebsiteInfo)
        stmt = stmt.where(WebsiteInfo.id == website_id)

        try:
            await self.session.execute(stmt)
            await self.session.commit()
        except SQLAlchemyError as error:
            logging.error(error, exc_info=True)
            raise ValueError(f"Error deleting WebsiteInfo id={website_id}")
