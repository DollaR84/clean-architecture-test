from abc import abstractmethod
from typing import Protocol

import domain


class CreateWebsitesInfo(Protocol):

    @abstractmethod
    async def create_websites(
            self,
            data: list[domain.ContactData],
    ) -> list[domain.ContactData]:
        ...
