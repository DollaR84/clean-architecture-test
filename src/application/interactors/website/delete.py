from application import interfaces


class DeleteWebsiteInfo:

    def __init__(self, gateway: interfaces.DeleteWebsiteInfo):
        self.gateway = gateway

    async def __call__(
            self,
            website_id: int,
    ):
        await self.gateway.delete_website(website_id)
