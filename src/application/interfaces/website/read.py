from abc import abstractmethod
from typing import Protocol

import domain


class GetWebsitesInfo(Protocol):

    @abstractmethod
    async def get_websites(
            self,
            params: domain.WebsitesFilterParams | None = None,
    ) -> list[domain.ContactData]:
        ...


class GetWebsiteInfo(Protocol):

    @abstractmethod
    async def get_website(
            self,
            params: domain.WebsiteFilterParams,
    ) -> domain.ContactData | None:
        ...
