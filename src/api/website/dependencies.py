from fastapi import Query

from .. import schemas


def get_website_filters(
        id: int | None = Query(None, nullable=True, description="Find by id website"),
        search_url: str | None = Query(None, nullable=True, description="Find by website url by full match"),
) -> schemas.WebsiteFilterParams:
    return schemas.WebsiteFilterParams(
        id=id,
        search_url=search_url,
    )


def get_websites_filters(
        search_url: str | None = Query(None, nullable=True, description="Find by website url by partial match"),
        offset: int | None = Query(None, nullable=True, description="offset for load data"),
        limit: int | None = Query(None, nullable=True, description="limit for load data"),
) -> schemas.WebsitesFilterParams:
    return schemas.WebsitesFilterParams(
        search_url=search_url,
        offset=offset,
        limit=limit,
    )
