from application import dto
from application.interactors import (
    CreateWebsitesInfo,
    GetWebsitesInfo,
)

from dishka.integrations.fastapi import DishkaRoute, FromDishka

from fastapi import APIRouter, Depends, status

from .dependencies import get_websites_filters

from .. import schemas


router = APIRouter(prefix="/websites", route_class=DishkaRoute)


@router.get(
    "/",
    description="Method for get data of websites",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.ContactData],
)
async def get_websites_info(
        interactor: FromDishka[GetWebsitesInfo],
        params: schemas.WebsitesFilterParams = Depends(get_websites_filters),
) -> list[schemas.ContactData]:
    params = dto.WebsitesFilterParams(**params.dict())
    results = await interactor(params)

    return [
        schemas.ContactData(**result.dict())
        for result in results
    ]


@router.post(
    "/",
    description="Method for save new websites",
    status_code=status.HTTP_201_CREATED,
)
async def save_websites_info(
        data: list[schemas.ContactData],
        interactor: FromDishka[CreateWebsitesInfo],
) -> list[schemas.ContactData]:
    data = [dto.ContactData(**item.dict()) for item in data]
    results = await interactor(data)
    return [schemas.ContactData(**item.dict()) for item in results]
