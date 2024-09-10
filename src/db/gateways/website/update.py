import logging

import domain

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from ..base import BaseGateway

from ...models import WebsiteInfo


class UpdateWebsiteInfo(BaseGateway):

    async def update_website(
            self,
            website_id: int,
            data: domain.UpdateContactData,
    ) -> domain.ContactData:
        stmt = select(WebsiteInfo)
        stmt = stmt.where(WebsiteInfo.id == website_id)

        website_info = await self.session.execute(stmt)
        website_info = website_info.scalar()

        if website_info is None:
            raise ValueError(f"WebsiteInfo with id={website_id} not found")

        update_data = {}
        if data.emails is not None:
            update_data["emails"] = data.emails_to_str()
        if data.phones is not None:
            update_data["phones"] = data.phones_to_str()

        try:
            for field, value in update_data.items():
                setattr(website_info, field, value)
            await self.session.commit()

            return domain.ContactData(**website_info.dict(exclude=["id"]))
        except SQLAlchemyError as error:
            logging.error(error, exc_info=True)
            raise ValueError(f"Error updating WebsiteInfo id={website_id}")
