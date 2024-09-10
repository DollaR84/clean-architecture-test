import csv
from functools import singledispatchmethod
import logging
import shutil

from application import dto
from application.interactors import CreateUploadFile, CreateWebsitesInfo

from config import Config

from fastapi import File


class UploadService:

    def __init__(
            self,
            config: Config,
            interactor_upload_file: CreateUploadFile,
            interactor_websites_info: CreateWebsitesInfo,
    ):
        self.config = config
        self.interactor_upload_file: CreateUploadFile = interactor_upload_file
        self.interactor_websites_info: CreateWebsitesInfo = interactor_websites_info

        self.urls: list[str] = []
        self.file_id: int | None = None

    def add_url(self, url: str):
        url = url.strip()
        if url:
            self.urls.append(url)

    @singledispatchmethod
    def load_urls(self, data):
        raise NotImplementedError("Cannot load urls")

    @load_urls.register
    def _(self, data: dto.UploadData):
        for url in data.urls:
            self.add_url(url)

    @load_urls.register
    def _(self, data: dto.UploadTxtFile):
        with open(data.filename, 'r', encoding='utf-8') as file_data:
            for line in file_data.readlines():
                self.add_url(line)

    @load_urls.register
    def _(self, data: dto.UploadCsvFile):
        csv_data = self._csv_file(data.filename)

        headers = next(csv_data).split(self.config.csv.delimiter)
        url_index = headers.index(self.config.csv.url_column_name)

        for row in csv_data:
            row_data = row.split(self.config.csv.delimiter)
            self.add_url(row_data[url_index])

    def _csv_file(self, filename: str):
        for row in self._csv_rows(filename):
            yield row

    def _csv_rows(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file_data:
            data = csv.reader(file_data, delimiter=self.config.csv.delimiter, quotechar=self.config.csv.quotechar)
            yield next(data)

            for row in data:
                yield row

    def _save_file(self, file: File, data: dto.UploadFile):
        try:
            with open(data.filename, 'wb') as data_file:
                shutil.copyfileobj(file, data_file)

        except Exception as error:
            logging.error(error, exc_info=True)
            logging.error(f"Error saving file: {data.filename}")

        finally:
            file.close()

    async def save_file(self, file: File, data: dto.UploadFile):
        self._save_file(file, data)
        result = await self.interactor_upload_file(data)
        self.file_id = result.id

    async def process(self):
        pass
