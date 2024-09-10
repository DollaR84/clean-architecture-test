from pydantic import BaseModel, Field

from fastapi import Query


class WebsiteFilterParams(BaseModel):
    id: int | None = Query(None, nullable=True)
    search_url: str | None = Field(default=None, nullable=True)


class WebsitesFilterParams(BaseModel):
    search_url: str | None = Field(default=None, nullable=True)
    offset: int | None = Query(None, nullable=True)
    limit: int | None = Query(None, nullable=True)
