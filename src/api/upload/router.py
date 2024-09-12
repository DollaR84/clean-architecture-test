import os

from application import dto
from application.services import UploadService

from config import Config

from dishka.integrations.fastapi import DishkaRoute, FromDishka

from fastapi import APIRouter, File, UploadFile, status

from .. import schemas


router = APIRouter(prefix="/upload", route_class=DishkaRoute)


@router.post(
    "/",
    description="Method for upload list urls for parsing",
    status_code=status.HTTP_200_OK,
)
async def load_urls(
        service: FromDishka[UploadService],
        data: schemas.UploadData,
):
    data = dto.UploadData(**data.dict())

    service.load_urls(data)
    await service.process()


@router.post(
    "/txt",
    description="Method for upload txt file with urls for parsing",
    status_code=status.HTTP_200_OK,
)
async def load_txt(
        service: FromDishka[UploadService],
        config: FromDishka[Config],
        file: UploadFile = File(...),
):
    data = dto.UploadTxtFile(filename=os.path.join(config.upload_folder, file.filename))

    service.load_urls(data)
    await service.save_file(file.file, data)
    await service.process()


@router.post(
    "/csv",
    description="Method for upload csv file with urls for parsing",
    status_code=status.HTTP_200_OK,
)
async def load_csv(
        service: FromDishka[UploadService],
        config: FromDishka[Config],
        file: UploadFile = File(...),
):
    data = dto.UploadCsvFile(filename=os.path.join(config.upload_folder, file.filename))

    service.load_urls(data)
    await service.save_file(file.file, data)
    await service.process()
