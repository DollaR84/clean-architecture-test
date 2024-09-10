from abc import abstractmethod
from typing import Protocol

import domain


class UpdateWebsiteInfo(Protocol):

    @abstractmethod
    async def update_website(
            self,
            website_id: int,
            data: domain.UpdateContactData,
    ) -> domain.ContactData:
        ...
