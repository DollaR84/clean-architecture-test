from application import dto
from application import interfaces

import domain


class GetWebsitesInfo:

    def __init__(self, gateway: interfaces.GetWebsitesInfo):
        self.gateway = gateway

    async def __call__(
            self,
            params: dto.WebsitesFilterParams | None = None,
    ) -> list[dto.ContactData]:
        params = domain.WebsitesFilterParams(**params.dict()) if params else params
        results = await self.gateway.get_websites(params)
        return [dto.ContactData(**item.dict()) for item in results]


class GetWebsiteInfo:

    def __init__(self, gateway: interfaces.GetWebsiteInfo):
        self.gateway = gateway

    async def __call__(
            self,
            params: dto.WebsiteFilterParams,
    ) -> dto.ContactData | None:
        params = domain.WebsiteFilterParams(**params.dict())
        result = await self.gateway.get_website(params)
        return dto.ContactData(**result.dict()) if result else result
