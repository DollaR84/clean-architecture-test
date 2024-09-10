from dataclasses import dataclass

from .base import BaseData


@dataclass(slots=True)
class WebsiteFilterParams(BaseData):
    id: int | None = None
    search_url: str | None = None


@dataclass(slots=True)
class WebsitesFilterParams(BaseData):
    search_url: str | None = None
    offset: int | None = None
    limit: int | None = None
