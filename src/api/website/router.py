from application import dto
from application.interactors import (
    CreateWebsitesInfo,
    DeleteWebsiteInfo,
    GetWebsiteInfo,
    UpdateWebsiteInfo,
)

from dishka.integrations.fastapi import DishkaRoute, FromDishka

from fastapi import APIRouter, Depends, status

from .dependencies import get_website_filters

from .. import schemas


router = APIRouter(prefix="website", route_class=DishkaRoute)


@router.get(
    "/",
    description="Method for find website",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ContactData | None,
)
async def get_website_info(
        interactor: FromDishka[GetWebsiteInfo],
        params: schemas.WebsiteFilterParams = Depends(get_website_filters),
) -> schemas.ContactData | None:
    params = dto.WebsiteFilterParams(**params.dict())
    result = await interactor(params)

    if result:
        result = schemas.ContactData(**result.dict())

    return result


@router.post(
    "/",
    description="Method for save new website",
    status_code=status.HTTP_201_CREATED,
)
async def save_website_info(
        data: schemas.ContactData,
        interactor: FromDishka[CreateWebsitesInfo],
) -> schemas.ContactData:
    data = dto.ContactData(**data.dict())
    results = await interactor([data])
    return schemas.ContactData(**results[0].dict())


@router.patch(
    "/{website_id}",
    description="Method for update website data",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_website_info(
        website_id: int,
        data: schemas.UpdateContactData,
        interactor: FromDishka[UpdateWebsiteInfo],
) -> schemas.ContactData:
    data = dto.UpdateContactData(**data.dict(exclude_unset=True))
    result = await interactor(website_id, data)
    return schemas.ContactData(**result.dict())


@router.delete(
    "/{website_id}",
    description="Method for delete website",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_website_info(
        website_id: int,
        interactor: FromDishka[DeleteWebsiteInfo],
):
    await interactor(website_id)
