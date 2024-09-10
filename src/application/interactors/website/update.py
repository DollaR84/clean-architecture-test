from application import dto
from application import interfaces

import domain


class UpdateWebsiteInfo:

    def __init__(self, gateway: interfaces.UpdateWebsiteInfo):
        self.gateway = gateway

    async def __call__(
            self,
            website_id: int,
            data: dto.UpdateContactData,
    ) -> dto.ContactData:
        data = domain.UpdateContactData(**data.dict())
        return await self.gateway.update_website(website_id, data)
