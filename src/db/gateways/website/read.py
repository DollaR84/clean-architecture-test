import domain

from sqlalchemy import select

from ..base import BaseGateway

from ...models import WebsiteInfo


class GetWebsitesInfo(BaseGateway):

    async def get_websites(
            self,
            params: domain.WebsitesFilterParams | None = None,
    ) -> list[domain.ContactData]:
        stmt = select(WebsiteInfo)

        if params and params.search_url:
            stmt = stmt.where(WebsiteInfo.website.contains(params.search_url.strip()))

        stmt = stmt.order_by(WebsiteInfo.id)

        if params and params.offset:
            stmt = stmt.offset(params.offset)
        if params and params.limit:
            stmt = stmt.limit(params.limit)

        websites_info = await self.session.execute(stmt)
        websites_info = websites_info.scalars() if websites_info else []

        return [
            domain.ContactData(**info.dict())
            for info in websites_info
        ]


class GetWebsiteInfo(BaseGateway):

    async def get_website(
            self,
            params: domain.WebsiteFilterParams,
    ) -> domain.ContactData | None:
        result = None
        if not any([params.id, params.search_url]):
            raise ValueError("Must specify one of the search parameters: 'id' or 'search_url'")

        stmt = select(WebsiteInfo)

        if params.id:
            stmt = stmt.where(WebsiteInfo.id == params.id)
        elif params.search_url:
            stmt = stmt.where(WebsiteInfo.website.contains(params.search_url.strip()))

        website_info = await self.session.execute(stmt)
        website_info = website_info.scalar()

        if website_info:
            result = domain.ContactData(**website_info.dict())

        return result
