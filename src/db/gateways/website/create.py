import logging

import domain

from sqlalchemy.exc import SQLAlchemyError

from ..base import BaseGateway

from ...models import WebsiteInfo


class CreateWebsitesInfo(BaseGateway):

    async def create_websites(
            self,
            data: list[domain.ContactData],
    ) -> list[domain.ContactData]:
        websites_info = [
            WebsiteInfo(
                website=item.website,
                emails=item.emails_to_str(),
                phones=item.phones_to_str(),
            ) for item in data
        ]

        try:
            for website_info in websites_info:
                self.session.add(website_info)
            await self.session.commit()

            return [
                domain.ContactData(**info.dict())
                for info in websites_info
            ]
        except SQLAlchemyError as error:
            logging.error(error, exc_info=True)
            raise ValueError("Error creating new WebsiteInfo records")
