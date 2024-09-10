from abc import abstractmethod
from typing import Protocol


class DeleteWebsiteInfo(Protocol):

    @abstractmethod
    async def delete_website(
            self,
            website_id: int,
    ):
        ...
