from application import dto
from application import interfaces

import domain


class CreateWebsitesInfo:

    def __init__(self, gateway: interfaces.CreateWebsitesInfo):
        self.gateway = gateway

    async def __call__(
            self,
            data: list[dto.ContactData],
    ):
        data = [domain.ContactData(**item.dict(exclude=["id"])) for item in data]
        results = await self.gateway.create_websites(data)
        return [dto.ContactData(**item.dict()) for item in results]
